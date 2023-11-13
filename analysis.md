Product :
    - name
    - description
    - image
    - images *
    - price
    - flag [sale-new-feature]
    - brand
    - sku
    - reviews : *
      - user
      - rate
      - feedback
      - creation date
    - subtitle
    - quantity
    - tags


brand : *
    - image
    - title
    - product_count
    - rate

    -------------------------------

orders : 
  - status [Recieved , Processed ، Shipped , Delivered]
  - code 
  - order_time
  - delivery_time
  - sub_total
  - discount 
  - delivery_fee
  - total
  - delivery_location 
  - quantity 

  - product
  - brand 
  - price 

