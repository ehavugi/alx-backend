#!/bin/bash
curl localhost:1245/list_products ; echo ""
# Product detail
curl localhost:1245/list_products/1 ; echo ""
#  expecting {"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4,"currentQuantity":4}
curl localhost:1245/list_products/12 ; echo ""
# if an item not exist {"status":"Product not found"}

## Reserve a product
#Create the route GET /reserve_product/:itemId:
# if the item does not exist, it should return:
curl localhost:1245/reserve_product/12 ; echo ""
# -- {"status":"Product not found"}


#If the item exists, it should check that there is at least one stock available. If not it should return:
curl localhost:1245/reserve_product/1 ; echo ""
#{"status":"Not enough stock available","itemId":1}
# If there is enough stock available, it should reserve one item (by using reserveStockById), and return:
curl localhost:1245/reserve_product/2 ; echo ""
#{"status":"Reservation confirmed","itemId":1}
