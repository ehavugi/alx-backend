import express from 'express';
import redis from 'redis';
import { promisify } from 'util';


const app = express();
const port = 1245;

// Initialize Redis client
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// List of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Function to store listProducts in Redis
async function storeListProductsInRedis() {
  try {
    await setAsync('listProducts', JSON.stringify(listProducts));
    console.log('List of products stored in Redis');
  } catch (error) {
    console.error('Error storing listProducts in Redis:', error);
  }
}

storeListProductsInRedis();

async function initializeReservesInRedis() {
  for (const product of listProducts) {
    const { itemId, initialAvailableQuantity } = product;
    await setAsync(`item.${itemId}`, initialAvailableQuantity.toString());
  }
  console.log('Reserves initialized in Redis');
}

// Call the initialization function when the server starts
initializeReservesInRedis();

// Function to get an item by ID
function getItemById(id) {
  console.log('get Item by id called ', id); 
  return listProducts.find((product) => product.itemId === id);
}

// Route to list all available products
app.get('/list_products', (req, res) => {
  const products = listProducts.map((product) => {
    return {
      itemId: product.itemId,
      itemName: product.itemName,
      price: product.price,
      initialAvailableQuantity: product.initialAvailableQuantity,
    };
  });
  res.json(products);
});

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  const productDetails = {
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity,
    currentQuantity,
  };

  res.json(productDetails);
});

// Function to reserve stock by item ID
async function reserveStockById(itemId, stock) {
   console.log('reserve stock: itemId, stock ', itemId, stock);
  await setAsync(`item.${itemId}`, stock);
}

// Function to get current reserved stock by item ID
async function getCurrentReservedStockById(itemId) {
  console.log('request to reserve', itemId);
  try {
    const reservedStock = await getAsync(`item.${itemId}`);
    return parseInt(reservedStock, 10) || 0;
  } catch (error) {
    console.error('Error retrieving current quantity from Redis:', error);
    return 0; // Return 0 when an error occurs
  }
}


// Route to reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);

  if (currentQuantity === 0) {
    return res.status(400).json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, currentQuantity - 1);

  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

export default app;
