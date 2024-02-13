def multi_shot_prompt(product_name, product_description):
    context = """This product data is for an online shop shown in search engines.
    You will receive \'Product Name\' and \'Product Description\' delimited by angle brackets.
    Your task is to generate a \'Meta Description\' to improve the SEO ranking.

    1. The \'Meta Description\' must be a JSON object with two fields: pageTitle, metaDescription.
    2. Write metaDescription in an active voice.
    3. Keep metaDescription concise, between 50 and 150 characters.
    4. pageTitle must not exceed 100 characters.
    5. Use %s language for both metaDescription and pageTitle."""

    multi_shot_examples = """Product Name and Product Description: Product Name: Alisha Solid Women\'s Cycling Shorts

    Product Description: Key Features of Alisha Solid Women\'s Cycling Shorts Cotton Lycra Navy, Red, Navy,Specifications of Alisha Solid Women\'s Cycling Shorts Shorts Details Number of Contents in Sales Package Pack of 3 Fabric Cotton Lycra Type Cycling Shorts General Details Pattern Solid Ideal For Women\'s Fabric Care Gentle Machine Wash in Lukewarm Water, Do Not Bleach Additional Details Style Code ALTHT_3P_21 In the Box 3 shorts
    Meta Description: {
    \"pageTitle\": \"Women\'s Cycling Shorts\",
    \"metaDescription\": \"Discover comfortable, cotton-lycra cycling shorts that offer a solid color and stay snug against your skin.\"
    }

    Product Name and Product Description: Product Name: FabHomeDecor Fabric Double Sofa Bed

    Product Description: FabHomeDecor Fabric Double Sofa Bed (Finish Color - Leatherette Black Mechanism Type - Pull Out) Price: Rs. 22,646 • Fine deep seating experience • Save Space with the all new click clack Sofa Bed • Easy to fold and vice versa with simple click clack mechanism • Chrome legs with mango wood frame for long term durability • Double cushioned Sofa Bed to provide you with extra softness to make a fine seating experience • A double bed that can easily sleep two,Specifications of FabHomeDecor Fabric Double Sofa Bed (Finish Color - Leatherette Black Mechanism Type - Pull Out) Installation & Demo Installation & Demo Details Installation and demo for this product is done free of cost as part of this purchase. Our service partner will visit your location within 72 business hours from the delivery of the product. In The Box 1 Sofa Bed General Brand FabHomeDecor Mattress Included No Delivery Condition Knock Down Storage Included No Mechanism Type Pull Out Type Sofa Bed Style Contemporary & Modern Filling Material Microfiber Seating Capacity 3 Seater Upholstery Type NA Upholstery Included No Bed Size Double Shape Square Suitable For Living Room Model Number FHD112 Care Instructions Avoid outdoor use and exposure to water or prolonged moisture, Avoid exposure to direct heat or sunlight as this can cause the sofa colour to fade, Keep sharp objects away from your sofa, A little tear on the fabric cover may be hard to repair, Vacuum your sofas periodically with a soft bristled bru...View More Avoid outdoor use and exposure to water or prolonged moisture, Avoid exposure to direct heat or sunlight as this can cause the sofa colour to fade, Keep sharp objects away from your sofa, A little tear on the fabric cover may be hard to repair, Vacuum your sofas periodically with a soft bristled brush attachment or lightly brush them to keep general dirt and dust off the sofa and prevent any embedding between the fibres, Try to avoid food and drink spillage of any kind, If spills occur, do not leave unattended, In case of a stain, a water-free fabric cleaner can be used, However, avoid applying the cleaner directly on the stain as this can cause damage to the fabric and fade colour, Pour the cleaner onto a clean cloth and test its effect on a hidden area of the sofa before cleaning the stain with the cloth, A professional scotchguard treatment is one of the easiest and most effective options to protect against spills or stains and keep pet hair at bay, Getting your sofa professionally cleaned once every 6-8 months will not only take care of the nooks and corners that you can\'t reach, it will also make it more durable Finish Type Matte Important Note Cancellation NOT allowed for this product after 24 hrs of order booking. Warranty Covered in Warranty Warranty covers all kind of manufacturing defects. Concerned product will either be repaired or replaced based on discretion. Service Type Manufacturer Warranty Warranty Summary 6 Months Domestic Warranty Not Covered in Warranty Warranty does not cover for Improper Handling Dimensions Weight 40 kg Height 838 mm Width 1905 mm Depth 939 mm Disclaimer - The color of the product may vary slightly compared to the picture displayed on your screen. This is due to lighting, pixel quality and color settings - Please check the product\'s dimensions to ensure the product will fit in the desired location. Also, check if the product will fit through...View More - The color of the product may vary slightly compared to the picture displayed on your screen. This is due to lighting, pixel quality and color settings - Please check the product\'s dimensions to ensure the product will fit in the desired location. Also, check if the product will fit through the entrance(s) and door(s) of the premises - Please expect an unevenness of up to 5 mm in the product due to differences in surfaces and floor levels - Flipkart, or the Seller delivering the product, will not take up any type of civil work, such as drilling holes in the wall to mount the product. The product will only be assembled in case carpentry assembly is required - In case the product appears to lack shine, wiping the surface with a cloth will help clear the surface of dust particles Material & Color Upholstery Color Leatherette Black Primary Color Black Primary Material Fabric Secondary Material Subtype Mango Wood Secondary Material Foam Finish Color Leatherette Black Primary Material Subtype Foam
    Meta Description: {
    \"pageTitle\": \"FabHomeDecor Fabric Double Sofa Bed\",
    \"metaDescription\": \"Transform this contemporary pull-out sofa bed into a double bed that effortlessly sleeps two.\"
    }


    Product Name and Product Description: Product Name: AW Bellies

    Product Description: Key Features of AW Bellies Sandals Wedges Heel Casuals,AW Bellies Price: Rs. 499 Material: Synthetic Lifestyle: Casual Heel Type: Wedge Warranty Type: Manufacturer Product Warranty against manufacturing defects: 30 days Care instructions: Allow your pair of shoes to air and de-odorize at regular basis; use shoe bags to prevent any stains or mildew; dust any dry dirt from the surface using a clean cloth; do not use polish or shiner,Specifications of AW Bellies General Ideal For Women Occasion Casual Shoe Details Color Red Outer Material Patent Leather Heel Height 1 inch Number of Contents in Sales Package Pack of 1 In the Box One Pair Of Shoes
    Meta Description: {
    \"pageTitle\": \"Red Wedge Sandals\",
    \"metaDescription\": \"Explore these casual, red wedge sandals offering comfort and style.\"
    }


    Product Name and Product Description: Product Name: Sicons All Purpose Arnica Dog Shampoo

    Product Description: Specifications of Sicons All Purpose Arnica Dog Shampoo (500 ml) General Pet Type Dog Brand Sicons Quantity 500 ml Model Number SH.DF-14 Type All Purpose Fragrance Arnica Form Factor Liquid In the Box Sales Package Shampoo Sicons Dog Fashion Arnica
    Meta Description: {
    \"pageTitle\": \"Sicons All Purpose Arnica Dog Shampoo\",
    \"metaDescription\": \"Keep your dog clean and fresh with this all-purpose arnica shampoo.\"
    }


    Product Name and Product Description: Product Name: Eternal Gandhi Super Series Crystal Paper Weights  with Silver Finish

    Product Description: Key Features of Eternal Gandhi Super Series Crystal Paper Weights  with Silver Finish Crystal  paper weight Product Dimensions :   8cm x  8cm x 5cm A beautiful product Material: Crystal,Eternal Gandhi Super Series Crystal Paper Weights  with Silver Finish (Set Of 1, Clear) Price: Rs. 430 Your office desk will sparkle and shine when you accent tables with this elegant crystal paper weight. The multifaceted crystal features Gandhiji’s bust and his timeless message – “My life is my message – M.K. Gandhi”. A beautiful product to gift to your near and dear ones in family and Business.,Specifications of Eternal Gandhi Super Series Crystal Paper Weights  with Silver Finish (Set Of 1, Clear) General Model Name Gandhi Paper Weight Mark V Dimensions Weight 323 g In the Box Paper Weight Paper Weight Features Paper Weight Material Crystal Paper Weight Finish Silver Finish
    Meta Description: {
    \"pageTitle\": \"Crystal Paperweight with Gandhi Bust\",
    \"metaDescription\": \"Add a touch of elegance to your desk with this crystal paperweight featuring Gandhi\'s bust and a timeless message.\"
    }"""

    user_query = """
    Product Name and Product Description:

    Product Name: {product_name}

    Product Description: {product_description}
    Meta Description:
    """

    return context + multi_shot_examples + user_query.format(product_name=product_name, product_description=product_description)

if __name__ == "__main__":
    print(multi_shot_prompt(product_name = "hello test product", product_description="hello test description"))