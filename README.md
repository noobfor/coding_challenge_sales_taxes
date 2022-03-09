# coding_challenge_sales_taxes


I assumed that the import tax is applicable on all products

I assumed that the rounding is being applied for each tax and not the overall price.

Because the example shopping baskets didnt put more than one of each product in the list, I did not cover the case if there is more than one of one product being added.
If more than one product would have been added, more specification about tax calculation would be needed. For example if the tax is being applied on each of the same product
or calculated on the overall cost of the whole number of one product.

For the rounding rules I assumed that because of the sales tax of 10%, rounding is being done by (10 * p)/100 and rounded up to the nearest 0.05.
Same applies to 5% for import taxes

For Output 3 I outputted "1 box of imported chocolate" instead of "1 imported box of chocolates" because of the given Input