#main flask app


#CLASS obtain_input
    #collects all necessary user input
        #cost_for_price if c4
        #sale_price and guidance_margin if street smart
            #sale_price-guidance_margin=cost_for_price #could be handled in html
        #desired_margin $
        #rebate_percentage xx.xx%
        #IF c4
            #desired_margin+cost_for_price=sale_price  #could be handled in html
        #sale_price_two is new sale price input by user after running first calculation of
        
        
        



#METHOD process_input
    #output:
        #rebate_total is rebate_percentage of sale price
        #actual_margin is (sale_price-rebate_total)-cost_for_price
        #allow user to add a new_sale_price or desired margin (cost_for_price+desired_margin=new_sale_price)
            #show
                #rebate_total and sale_price with rebate total added to sale_price
                #margin with rebate_total inclusive of sale_price
                #margin as % and as $ where necessary
                #actual selling price as margin invoice margin is calculated, sale_price - rebate_total
                #adjust_margin after rebate_total and cost_for_price are removed from sale_price
                #margin_percent before rebate applied to sale_price
                #margin_percent after rebate applied to sale_price
                #margin_impact_perc and margin_impact_doll at adjusted_maargin
                #percent change
        #price adjustment
            #if actual_selling_price <5% above cost_for_price, recommend adjusting price or show options at 5.01%, 7%, 12%
            #both as rounded dollar $xx.xx and as a percentage or user can just change any of the mutable fields above

#will need some sort of clear the inputs function
            
            
        
