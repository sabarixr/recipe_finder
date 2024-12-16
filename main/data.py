ingredients = [
    "Egg", "Milk", "Flour", "Sugar", "Butter", "Banana", "Chicken", "Rice", "Tomato", "Onion", 
    "Garlic", "Cheese", "Spinach", "Carrot", "Potato", "Beef", "Fish", "Salt", "Pepper", "Oil",
    # Asian cuisine
    "Soy sauce", "Ginger", "Lemongrass", "Sesame oil", "Tofu", "Noodles", "Miso paste", "Sake", 
    "Fish sauce", "Hoisin sauce", "Bok choy", "Shiitake mushrooms", "Seaweed", "Wasabi", "Soba", 
    "Sriracha", "Coconut milk", "Tamarind", "Curry paste", "Water chestnuts", "Rice vinegar", 
    "Kimchi", "Gochujang", "Udon", "Ramen noodles", "Daikon", "Lotus root", "Bamboo shoots", 
    "Chinese cabbage", "Sichuan peppercorn", "Thai basil", "Galangal", "Star anise", "Fermented black beans", 
    "Dashi", "Pickled ginger",
    # Italian cuisine
    "Olive oil", "Basil", "Oregano", "Thyme", "Parmesan", "Mozzarella", "Prosciutto", "Capers", 
    "Pine nuts", "Balsamic vinegar", "Ricotta", "Pancetta", "Gnocchi", "Anchovies", "Polenta", "Pesto", 
    "Gorgonzola", "Pecorino Romano", "Burrata", "Marsala wine", "Cannellini beans", "Farro", "Arborio rice", 
    "Prosciutto di Parma", "Marscapone", "Radicchio", "Zucchini", "Artichoke", "Porcini mushrooms", 
    "Porchetta", "Grappa", "Sun-dried tomatoes",
    # Indian cuisine
    "Cumin", "Coriander", "Turmeric", "Garam masala", "Fenugreek", "Cardamom", "Mustard seeds", 
    "Ghee", "Paneer", "Lentils", "Chickpeas", "Curry leaves", "Tamarind", "Coconut", "Basmati rice", 
    "Cashews", "Green chili", "Fennel seeds", "Black mustard seeds", "Asafoetida (Hing)", "Saffron", 
    "Jaggery", "Black cardamom", "Star anise", "Curry powder", "Amchur (dried mango powder)", "Kokum", 
    "Tamarind paste", "Black salt (Kala Namak)",
    # Mexican cuisine
    "Corn", "Black beans", "Pinto beans", "Jalapeño", "Avocado", "Tortilla", "Lime", "Cilantro", 
    "Chipotle", "Salsa", "Chorizo", "Queso fresco", "Hominy", "Adobo sauce", "Refried beans",
    # Middle Eastern cuisine
    "Tahini", "Sumac", "Pomegranate molasses", "Za'atar", "Feta", "Bulgur", "Couscous", "Chickpeas", 
    "Lamb", "Pistachios", "Dates", "Rosewater", "Yogurt", "Saffron", "Pine nuts", "Lentils", "Cucumber",
    # French cuisine
    "Baguette", "Crème fraîche", "Dijon mustard", "Tarragon", "Leeks", "Shallots", "White wine", 
    "Butter", "Truffle", "Duck", "Thyme", "Herbs de Provence", "Cognac", "Bouillon", "Béchamel", 
    "Cornichons",
    # African cuisine
    "Plantains", "Cassava", "Okra", "Sorghum", "Millet", "Peanut butter", "Scotch bonnet", "Berbere", 
    "Harissa", "Fonio", "Egusi", "Baobab", "Teff", "Cloves", "Cinnamon",
    # Latin American cuisine
    "Yucca", "Achiote", "Papaya", "Mango", "Passion fruit", "Tapioca", "Quinoa", "Pork", "Red beans", 
    "Salsa Verde", "Chimichurri", "Cumin", "Epazote",
    'Cream of mushroom soup', 'Kidney beans', 'Lime leaves', 'Apple', 'Bacon', 'Mint', 'Crab', 'Gojujang',
     'Hummus', 'Mayonnaise', 'Pasta', 'Semolina', 'Mushrooms', 'Sushi rice', 'Mayo', 'Pork bones',
    'Broth', 'Lasagna noodles', 'Chicken wings', 'Ground beef', 'Bean sprouts', 'Green beans', 'Mascarpone',
    'Oaxaca cheese', 'Green salsa', 'Tortilla chips', 'Chili flakes', 'Bread', 'Rosemary', 'Cocoa powder',
    'Peanut', 'Pickled vegetables', 'Chili pepper', 'Rice paper', 'Vermicelli', 'Nori', 'Coffee', 'Sesame seeds',
    'Parsley', 'Salmon', 'Spaghetti', 'Paprika', 'Pumpkin', 'Bell peppers', 'Chocolate', 'Rice cakes', 'Gram flour',
    'Nutmeg', 'Falafel', 'Clams', 'Peanuts', 'Sour cream', 'Cheddar', 'Beans', 'Romaine lettuce', 'Macaroni', 'Honey',
    'Green onion', 'Water', 'Breadcrumbs', 'Lemon', 'Chili powder', 'Dumpling wrappers', 'Curry sauce', 'Grapes', 'Pineapple',
    'Cornmeal', 'Bell pepper', 'Peanut sauce', 'Cauliflower', 'Rice flour', 'Caesar dressing', 'Bun', 'Tater tots', 'Pickles',
    'Lettuce', 'Cayenne pepper', 'Brown sugar', 'Pork belly', 'Baking powder', 'Spices', 'Rice noodles', 'Dashi broth', 'Bay leaves',
    'Cabbage', 'Chili oil', 'Fish cakes', 'Corn tortilla', 'Ketchup', 'Chickpea flour', 'Orange', 'Chili', 'Shrimp', 'Peas', 'Napa cabbage', 
    'Beef broth', 'Lemon juice', 'Hot sauce', 'Mustard', 'Green curry paste', 'Celery', 'Pizza dough', 'Tuna', 'Croutons', 'Broccoli', 'Corn husks',
    'Spring onion', 'Eggplant', 'Tomato sauce', 'Panko', 'Cream', 'Green peas', 'Barbecue sauce', 'Masa harina', 'Olives', 'Vinegar'
]
recipes = {
    "Pancake": {
        "ingredients": ["Egg", "Milk", "Flour", "Sugar", "Butter"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": ["low-carb", "gluten-free"],
        "cuisine": "American"
    },
    "Omelette": {
        "ingredients": ["Egg", "Cheese", "Onion", "Salt", "Pepper"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based"],
        "cuisine": "American"
    },
    "Smoothie": {
        "ingredients": ["Milk", "Banana", "Honey", "Yogurt"],
        "difficulty": 1,
        "prep_time": 5,
        "dietary_compatibility": ["plant-based"],
        "cuisine": "American"
    },
    "Cake": {
        "ingredients": ["Egg", "Milk", "Flour", "Sugar", "Butter"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["low-carb"],
        "cuisine": "American"
    },
    "Chicken Curry": {
        "ingredients": ["Chicken", "Tomato", "Onion", "Garlic", "Oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Guacamole": {
        "ingredients": ["Avocado", "Lime", "Onion", "Salt", "Cilantro"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based", "gluten-free", "low-carb"],
        "cuisine": "Mexican"
    },
    "Vegetable Stir-Fry": {
        "ingredients": ["Broccoli", "Carrot", "Garlic", "Soy sauce", "Sesame oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Asian"
    },
    "Beef Stew": {
        "ingredients": ["Beef", "Carrot", "Onion", "Garlic", "Potato"],
        "difficulty": 4,
        "prep_time": 120,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "American"
    },
    "Fish Tacos": {
        "ingredients": ["Fish", "Tortilla", "Cabbage", "Lime", "Cilantro"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Greek Salad": {
        "ingredients": ["Cucumber", "Tomato", "Feta", "Olive oil", "Olives"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based", "gluten-free", "low-carb"],
        "cuisine": "Mediterranean"
    },
    "Pad Thai": {
        "ingredients": ["Rice noodles", "Tofu", "Egg", "Fish sauce", "Peanuts"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Thai"
    },
    "Tomato Basil Pasta": {
        "ingredients": ["Pasta", "Tomato", "Basil", "Olive oil", "Garlic"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based"],
        "cuisine": "Italian"
    },
    "Shakshuka": {
        "ingredients": ["Egg", "Tomato", "Onion", "Garlic", "Bell pepper"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Middle Eastern"
    },
    "Chana Masala": {
        "ingredients": ["Chickpeas", "Tomato", "Onion", "Garlic", "Cumin"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Indian"
    },

    "Coconut Rice": {
        "ingredients": ["Rice", "Coconut milk", "Salt", "Sugar", "Water"],
        "difficulty": 1,
        "prep_time": 25,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Asian"
    },
    "Tacos Al Pastor": {
        "ingredients": ["Pork", "Pineapple", "Tortilla", "Onion", "Cilantro"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Miso Soup": {
        "ingredients": ["Miso paste", "Tofu", "Seaweed", "Green onion", "Dashi"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Japanese"
    },
    "Ratatouille": {
        "ingredients": ["Eggplant", "Zucchini", "Tomato", "Onion", "Garlic"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["plant-based", "gluten-free", "low-carb"],
        "cuisine": "French"
    },
    "Spinach and Ricotta Ravioli": {
        "ingredients": ["Spinach", "Ricotta", "Flour", "Egg", "Parmesan"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": [],
        "cuisine": "Italian"
    },
    "Fried Rice": {
        "ingredients": ["Rice", "Egg", "Soy sauce", "Garlic", "Onion"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": [],
        "cuisine": "Asian"
    },
    "Sushi Rolls": {
        "ingredients": ["Rice", "Nori", "Fish", "Cucumber", "Avocado"],
        "difficulty": 3,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Japanese"
    },
    "Tiramisu": {
        "ingredients": ["Mascarpone", "Egg", "Sugar", "Coffee", "Cocoa powder"],
        "difficulty": 4,
        "prep_time": 120,
        "dietary_compatibility": [],
        "cuisine": "Italian"
    },
    "Eggplant Parmesan": {
        "ingredients": ["Eggplant", "Tomato sauce", "Mozzarella", "Parmesan", "Basil"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Italian"
    },
    "Gazpacho": {
        "ingredients": ["Tomato", "Cucumber", "Bell pepper", "Garlic", "Olive oil"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["plant-based", "gluten-free", "low-carb"],
        "cuisine": "Spanish"
    },
    "Lamb Kebabs": {
        "ingredients": ["Lamb", "Garlic", "Cumin", "Onion", "Parsley"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Middle Eastern"
    },
    "Pesto Pasta": {
        "ingredients": ["Basil", "Pine nuts", "Parmesan", "Garlic", "Olive oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based"],
        "cuisine": "Italian"
    },
    "Biryani": {
        "ingredients": ["Rice", "Chicken", "Yogurt", "Onion", "Spices"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Spaghetti Bolognese": {
        "ingredients": ["Spaghetti", "Beef", "Tomato", "Onion", "Garlic"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": [],
        "cuisine": "Italian"
    },
    "Fried Chicken": {
        "ingredients": ["Chicken", "Flour", "Egg", "Oil", "Salt"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Shrimp Scampi": {
        "ingredients": ["Shrimp", "Garlic", "Butter", "Lemon", "Pasta"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Italian"
    },
    "Grilled Cheese Sandwich": {
        "ingredients": ["Bread", "Cheese", "Butter"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Caesar Salad": {
        "ingredients": ["Romaine lettuce", "Parmesan", "Croutons", "Caesar dressing"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["low-carb"],
        "cuisine": "Italian"
    },
    "Margherita Pizza": {
        "ingredients": ["Pizza dough", "Tomato", "Mozzarella", "Basil"],
        "difficulty": 3,
        "prep_time": 25,
        "dietary_compatibility": [],
        "cuisine": "Italian"
    },
    "Lasagna": {
        "ingredients": ["Lasagna noodles", "Beef", "Ricotta", "Tomato sauce", "Parmesan"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": [],
        "cuisine": "Italian"
    },
    "Chicken Alfredo": {
        "ingredients": ["Chicken", "Pasta", "Butter", "Cream", "Parmesan"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "Italian"
    },
    "Tuna Salad": {
        "ingredients": ["Tuna", "Mayo", "Celery", "Onion", "Salt"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "American"
    },
    "French Toast": {
        "ingredients": ["Egg", "Milk", "Bread", "Cinnamon", "Butter"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Ramen": {
        "ingredients": ["Ramen noodles", "Egg", "Soy sauce", "Chicken broth", "Green onion"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": [],
        "cuisine": "Japanese"
    },
    "Clam Chowder": {
        "ingredients": ["Clams", "Potato", "Cream", "Onion", "Bacon"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Teriyaki Chicken": {
        "ingredients": ["Chicken", "Soy sauce", "Sugar", "Garlic", "Ginger"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Japanese"
    },
    "Mac and Cheese": {
        "ingredients": ["Macaroni", "Cheddar", "Butter", "Milk", "Flour"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Stuffed Peppers": {
        "ingredients": ["Bell pepper", "Rice", "Beef", "Tomato", "Cheese"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "American"
    },

    "Potato Salad": {
        "ingredients": ["Potato", "Mayo", "Mustard", "Celery", "Onion"],
        "difficulty": 1,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "American"
    },
    "Chicken Wings": {
        "ingredients": ["Chicken wings", "Hot sauce", "Butter", "Garlic", "Celery"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Lamb Chops": {
        "ingredients": ["Lamb", "Garlic", "Rosemary", "Olive oil", "Salt"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Middle Eastern"
    },
    "Cobb Salad": {
        "ingredients": ["Lettuce", "Bacon", "Chicken", "Egg", "Avocado"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "American"
    },
    "Quesadilla": {
        "ingredients": ["Tortilla", "Cheese", "Chicken", "Onion", "Bell pepper"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": [],
        "cuisine": "Mexican"
    },
    "Frittata": {
        "ingredients": ["Egg", "Onion", "Potato", "Cheese", "Spinach"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Italian"
    },
    "Pulled Pork Sandwich": {
        "ingredients": ["Pork", "BBQ sauce", "Bun", "Onion", "Pickle"],
        "difficulty": 4,
        "prep_time": 120,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Burrito": {
        "ingredients": ["Tortilla", "Beef", "Rice", "Cheese", "Beans"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "Mexican"
    },
    "Pho": {
        "ingredients": ["Rice noodles", "Beef", "Ginger", "Garlic", "Star anise"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Vietnamese"
    },
    "Crab Cakes": {
        "ingredients": ["Crab", "Breadcrumbs", "Egg", "Mayonnaise", "Dijon mustard"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Egg Salad": {
        "ingredients": ["Egg", "Mayo", "Mustard", "Onion", "Celery"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "American"
    },
    "Chicken Parmesan": {
        "ingredients": ["Chicken", "Parmesan", "Breadcrumbs", "Tomato sauce", "Mozzarella"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": [],
        "cuisine": "Italian"
    },
    "Minestrone": {
        "ingredients": ["Pasta", "Tomato", "Carrot", "Onion", "Beans"],
        "difficulty": 2,
        "prep_time": 35,
        "dietary_compatibility": [],
        "cuisine": "Italian"
    },
    "Pesto Chicken": {
        "ingredients": ["Chicken", "Basil", "Pine nuts", "Garlic", "Parmesan"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Italian"
    },
    "French Onion Soup": {
        "ingredients": ["Onion", "Beef broth", "Cheese", "Bread", "Butter"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": [],
        "cuisine": "French"
    },
    "Eggplant Stir-Fry": {
        "ingredients": ["Eggplant", "Soy sauce", "Garlic", "Ginger", "Sesame oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Asian"
    },
    "Shepherd's Pie": {
        "ingredients": ["Beef", "Potato", "Carrot", "Onion", "Peas"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "British"
    },
    "Cornbread": {
        "ingredients": ["Cornmeal", "Flour", "Egg", "Milk", "Butter"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Falafel Wrap": {
        "ingredients": ["Falafel", "Tortilla", "Lettuce", "Tomato", "Hummus"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based"],
        "cuisine": "Middle Eastern"
    },
    "Chicken Shawarma": {
        "ingredients": ["Chicken", "Garlic", "Yogurt", "Cumin", "Paprika"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Middle Eastern"
    },
    "Chicken Caesar Wrap": {
        "ingredients": ["Tortilla", "Chicken", "Caesar dressing", "Lettuce", "Parmesan"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Tuna Melt": {
        "ingredients": ["Tuna", "Cheese", "Bread", "Mayo", "Onion"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Sloppy Joes": {
        "ingredients": ["Beef", "Tomato sauce", "Bun", "Onion", "Mustard"],
        "difficulty": 3,
        "prep_time": 25,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Pork Tacos": {
        "ingredients": ["Pork", "Tortilla", "Onion", "Cilantro", "Salsa"],
        "difficulty": 3,
        "prep_time": 35,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Broccoli Cheddar Soup": {
        "ingredients": ["Broccoli", "Cheddar", "Cream", "Butter", "Onion"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "American"
    },
    "Chicken Fajitas": {
        "ingredients": ["Chicken", "Bell pepper", "Onion", "Tortilla", "Sour cream"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "Mexican"
    },
    "Caprese Salad": {
        "ingredients": ["Tomato", "Mozzarella", "Basil", "Olive oil", "Balsamic vinegar"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Italian"
    },
    "Pancit": {
        "ingredients": ["Rice noodles", "Chicken", "Cabbage", "Carrot", "Soy sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Philippine"
    },
    "Pork Schnitzel": {
        "ingredients": ["Pork", "Breadcrumbs", "Egg", "Flour", "Lemon"],
        "difficulty": 3,
        "prep_time": 25,
        "dietary_compatibility": [],
        "cuisine": "German"
    },
    "Chicken Pot Pie": {
        "ingredients": ["Chicken", "Carrot", "Onion", "Flour", "Butter"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": [],
        "cuisine": "American"
    },
    "Shrimp Fried Rice": {
        "ingredients": ["Shrimp", "Rice", "Egg", "Soy sauce", "Onion"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": [],
        "cuisine": "Asian"
    },
    "Pad Thai": {
        "ingredients": ["Rice noodles", "Shrimp", "Egg", "Peanut", "Bean sprouts", "Fish sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Thai"
    },
    "Sushi Rolls": {
        "ingredients": ["Sushi rice", "Nori", "Tuna", "Avocado", "Cucumber", "Soy sauce"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Japanese"
    },
    "Beef Bulgogi": {
        "ingredients": ["Beef", "Soy sauce", "Garlic", "Onion", "Sesame oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": [],
        "cuisine": "Korean"
    },
    "Pho Ga (Chicken Pho)": {
        "ingredients": ["Chicken", "Rice noodles", "Ginger", "Star anise", "Cilantro"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Vietnamese"
    },
    "Miso Soup": {
        "ingredients": ["Miso paste", "Tofu", "Seaweed", "Green onion", "Dashi broth"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Japanese"
    },
    "Kung Pao Chicken": {
        "ingredients": ["Chicken", "Soy sauce", "Peanut", "Bell pepper", "Chili pepper"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Chinese"
    },
    "Tacos al Pastor": {
        "ingredients": ["Pork", "Tortilla", "Pineapple", "Onion", "Cilantro"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Chilaquiles": {
        "ingredients": ["Tortilla chips", "Egg", "Salsa", "Cheese", "Onion"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Pozole": {
        "ingredients": ["Pork", "Hominy", "Chili pepper", "Onion", "Cabbage"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Tamales": {
        "ingredients": ["Corn husks", "Masa harina", "Pork", "Chili pepper", "Cheese"],
        "difficulty": 5,
        "prep_time": 180,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Bibimbap": {
        "ingredients": ["Rice", "Beef", "Egg", "Spinach", "Carrot", "Gochujang"],
        "difficulty": 4,
        "prep_time": 50,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Korean"
    },
    "Chicken Katsu": {
        "ingredients": ["Chicken", "Panko", "Egg", "Flour", "Cabbage"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "Japanese"
    },
    "Thai Green Curry": {
        "ingredients": ["Coconut milk", "Chicken", "Green curry paste", "Basil", "Lime leaves"],
        "difficulty": 4,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Thai"
    },
    "Banh Mi": {
        "ingredients": ["Baguette", "Pork", "Pickled vegetables", "Cucumber", "Cilantro"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "Vietnamese"
    },
    "Teriyaki Salmon": {
        "ingredients": ["Salmon", "Soy sauce", "Sugar", "Garlic", "Ginger"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free", "sugar-free"],
        "cuisine": "Japanese"
    },
    "Sesame Chicken": {
        "ingredients": ["Chicken", "Soy sauce", "Sesame oil", "Honey", "Sesame seeds"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free", "sugar-free"],
        "cuisine": "Chinese"
    },
    "Roti Canai": {
        "ingredients": ["Flour", "Butter", "Milk", "Curry sauce"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": [],
        "cuisine": "Malaysian"
    },
    "Enchiladas Verdes": {
        "ingredients": ["Tortilla", "Chicken", "Green salsa", "Cheese", "Sour cream"],
        "difficulty": 3,
        "prep_time": 35,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Korean Kimchi Stew (Kimchi Jjigae)": {
        "ingredients": ["Kimchi", "Pork belly", "Tofu", "Onion", "Gochujang"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Korean"
    },
    "Yakitori (Grilled Chicken Skewers)": {
        "ingredients": ["Chicken", "Soy sauce", "Sake", "Sugar", "Green onion"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Japanese"
    },
    "Tonkotsu Ramen": {
        "ingredients": ["Pork bones", "Ramen noodles", "Egg", "Soy sauce", "Green onion"],
        "difficulty": 5,
        "prep_time": 180,
        "dietary_compatibility": [],
        "cuisine": "Japanese"
    },
    "Vietnamese Spring Rolls": {
        "ingredients": ["Rice paper", "Shrimp", "Mint", "Cucumber", "Vermicelli"],
        "difficulty": 3,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Vietnamese"
    },
    "Moo Shu Pork": {
        "ingredients": ["Pork", "Egg", "Cabbage", "Mushrooms", "Hoisin sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "Chinese"
    },
    "Mexican Street Tacos": {
        "ingredients": ["Corn tortilla", "Beef", "Onion", "Cilantro", "Lime"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Mexican"
    },
    "Gyoza (Japanese Dumplings)": {
        "ingredients": ["Pork", "Cabbage", "Garlic", "Ginger", "Dumpling wrappers"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "Japanese"
    },
    "Bibingka (Filipino Rice Cake)": {
        "ingredients": ["Rice flour", "Coconut milk", "Sugar", "Egg", "Butter"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free", "sugar-free"],
        "cuisine": "Filipino"
    },
    "Khao Pad (Thai Fried Rice)": {
        "ingredients": ["Rice", "Egg", "Garlic", "Soy sauce", "Shrimp"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": [],
        "cuisine": "Thai"
    },
    "Tlayuda (Oaxacan Pizza)": {
        "ingredients": ["Tortilla", "Black beans", "Oaxaca cheese", "Avocado", "Cilantro"],
        "difficulty": 3,
        "prep_time": 35,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Chinese Hot Pot": {
        "ingredients": ["Beef", "Tofu", "Mushrooms", "Bok choy", "Broth"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Chinese"
    },
    "Vietnamese Pho Bo (Beef Pho)": {
        "ingredients": ["Beef", "Rice noodles", "Cinnamon", "Star anise", "Cilantro"],
        "difficulty": 5,
        "prep_time": 120,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Vietnamese"
    },
    "Tamago Sushi (Egg Sushi)": {
        "ingredients": ["Egg", "Sushi rice", "Nori", "Soy sauce"],
        "difficulty": 3,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Japanese"
    },
    "Elote (Mexican Street Corn)": {
        "ingredients": ["Corn", "Mayonnaise", "Chili powder", "Lime", "Cheese"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Mexican"
    },
    "Banh Bao (Vietnamese Steamed Buns)": {
        "ingredients": ["Flour", "Pork", "Mushrooms", "Egg", "Coriander"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": [],
        "cuisine": "Vietnamese"
    },
    "Fish Tacos": {
        "ingredients": ["Fish", "Tortilla", "Cabbage", "Lime", "Avocado"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Mexican"
    },
    "Beef Tacos": {
        "ingredients": ["Beef", "Tortilla", "Cheese", "Sour cream", "Lettuce"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Mexican"
    },
    "Kung Pao Shrimp": {
        "ingredients": ["Shrimp", "Peanuts", "Bell pepper", "Soy sauce", "Chili pepper"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Chinese"
    },
    "Mole Poblano": {
        "ingredients": ["Chicken", "Chili pepper", "Tomato", "Chocolate", "Garlic"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": [],
        "cuisine": "Mexican"
    },
    "Chow Mein": {
        "ingredients": ["Noodles", "Chicken", "Cabbage", "Carrot", "Soy sauce"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": [],
        "cuisine": "Chinese"
    },
    "Spring Rolls": {
        "ingredients": ["Rice paper", "Shrimp", "Cabbage", "Carrot", "Mint"],
        "difficulty": 3,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Vietnamese"
    },
    "Carnitas": {
        "ingredients": ["Pork", "Onion", "Cilantro", "Lime", "Salsa"],
        "difficulty": 3,
        "prep_time": 35,
        "dietary_compatibility": ["gluten-free", "low-carb"],
        "cuisine": "Mexican"
    },


    "Sichuan Hot Pot": {
        "ingredients": ["Beef", "Tofu", "Cabbage", "Chili oil", "Mushrooms"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Chinese"
    },
    "Bibimbap": {
        "ingredients": ["Rice", "Beef", "Egg", "Spinach", "Carrot", "Gochujang"],
        "difficulty": 4,
        "prep_time": 50,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Korean"
    },
    "Nasi Goreng": {
        "ingredients": ["Rice", "Egg", "Chicken", "Carrot", "Soy sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "Indonesian"
    },
    "Tom Yum Soup": {
        "ingredients": ["Shrimp", "Lemongrass", "Lime leaves", "Chili", "Fish sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Thai"
    },
    "Burritos": {
        "ingredients": ["Tortilla", "Beef", "Rice", "Cheese", "Sour cream"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": [],
        "cuisine": "Mexican"
    },
    "Fajitas": {
        "ingredients": ["Chicken", "Bell pepper", "Onion", "Tortilla", "Lime"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": [],
        "cuisine": "Mexican"
    },
    "Pork Adobo": {
        "ingredients": ["Pork", "Soy sauce", "Vinegar", "Garlic", "Bay leaves"],
        "difficulty": 3,
        "prep_time": 60,
        "dietary_compatibility": [],
        "cuisine": "Filipino"
    },
    "Gado-Gado": {
        "ingredients": ["Tofu", "Cabbage", "Peanut sauce", "Carrot", "Egg"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based"],
        "cuisine": "Indonesian"
    },

    "Dim Sum": {
        "ingredients": ["Pork", "Shrimp", "Dumpling wrappers", "Ginger", "Soy sauce"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": [],
        "cuisine": "Chinese"
    },
    "Churros": {
        "ingredients": ["Flour", "Sugar", "Egg", "Butter", "Cinnamon"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": [],
        "cuisine": "Spanish"
    },
    "Arroz con Pollo": {
        "ingredients": ["Chicken", "Rice", "Tomato", "Garlic", "Peas"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": [],
        "cuisine": "Latin American"
    },
    "Ceviche": {
        "ingredients": ["Fish", "Lime", "Tomato", "Cilantro", "Onion"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Peruvian"
    },
    "Dosa": {
        "ingredients": ["Rice", "Flour", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 90,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Sambar": {
        "ingredients": ["Lentils", "Tomato", "Onion", "Garlic", "Carrot", "Tamarind", "Coriander", "Curry leaves"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Indian"
    },
    "Idli": {
        "ingredients": ["Rice", "Flour", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 120,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Vada": {
        "ingredients": ["Lentils", "Onion", "Coriander", "Curry leaves", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Upma": {
        "ingredients": ["Semolina", "Onion", "Carrot", "Peas", "Curry leaves", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Pongal": {
        "ingredients": ["Rice", "Lentils", "Pepper", "Ginger", "Curry leaves", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Masala Dosa": {
        "ingredients": ["Rice", "Flour", "Salt", "Oil", "Potato", "Onion", "Mustard seeds", "Curry leaves"],
        "difficulty": 3,
        "prep_time": 120,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Avial": {
        "ingredients": ["Carrot", "Potato", "Pumpkin", "Green beans", "Coconut", "Curry leaves", "Tamarind", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Indian"
    },
    "Rasam": {
        "ingredients": ["Tomato", "Garlic", "Tamarind", "Coriander", "Curry leaves", "Pepper", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Indian"
    },
    "Coconut Chutney": {
        "ingredients": ["Coconut", "Green chili", "Coriander", "Salt", "Oil", "Mustard seeds", "Curry leaves"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Indian"
    },
    "Mysore Pak": {
        "ingredients": ["Gram flour", "Sugar", "Butter", "Oil"],
        "difficulty": 4,
        "prep_time": 45,
        "dietary_compatibility": [],
        "cuisine": "Indian"
    },
    "Kootu": {
        "ingredients": ["Lentils", "Carrot", "Pumpkin", "Coconut", "Curry leaves", "Chili", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Indian"
    },
    "Bisi Bele Bath": {
        "ingredients": ["Rice", "Lentils", "Carrot", "Tomato", "Tamarind", "Curry leaves", "Mustard seeds", "Ginger", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Kadhi": {
        "ingredients": ["Yogurt", "Chili", "Curry leaves", "Mustard seeds", "Garlic", "Turmeric", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Daal": {
        "ingredients": ["Lentils", "Onion", "Garlic", "Ginger", "Tomato", "Curry leaves", "Chili", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Indian"
    },
    "Pakora": {
        "ingredients": ["Chickpea flour", "Onion", "Potato", "Chili", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Kulfi": {
        "ingredients": ["Milk", "Sugar", "Cardamom", "Pistachio"],
        "difficulty": 2,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Mango Lassi": {
        "ingredients": ["Yogurt", "Mango", "Honey", "Cardamom"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["gluten-free"],
        "cuisine": "Indian"
    },
    "Pulled Pork Sandwich": {
        "ingredients": ["Pork", "Bun", "Barbecue sauce", "Cabbage", "Pickles"],
        "difficulty": 3,
        "prep_time": 120,
        "dietary_compatibility": ["high-protein"],
        "cuisine": "American"
    },
    "Tater Tot Casserole": {
        "ingredients": ["Ground beef", "Tater tots", "Cheese", "Onion", "Cream of mushroom soup"],
        "difficulty": 3,
        "prep_time": 60,
        "dietary_compatibility": ["comfort-food"],
        "cuisine": "American"
    },
    "Sloppy Joes": {
        "ingredients": ["Ground beef", "Tomato", "Onion", "Ketchup", "Bread", "Mustard", "Brown sugar"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["high-protein"],
        "cuisine": "American"
    },
    "Pumpkin Pie": {
        "ingredients": ["Pumpkin", "Sugar", "Flour", "Butter", "Egg", "Cinnamon", "Nutmeg"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": ["dessert"],
        "cuisine": "American"
    },
    "Cornbread": {
        "ingredients": ["Cornmeal", "Flour", "Sugar", "Butter", "Egg", "Milk", "Baking powder"],
        "difficulty": 2,
        "prep_time": 40,
        "dietary_compatibility": ["comfort-food"],
        "cuisine": "American"
    },
    "BLT Sandwich": {
        "ingredients": ["Bacon", "Lettuce", "Tomato", "Bread", "Mayonnaise"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["high-protein"],
        "cuisine": "American"
    },
    "Fried Rice": {
        "ingredients": ["Rice", "Egg", "Onion", "Garlic", "Soy sauce", "Peas", "Carrot", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free", "high-protein"],
        "cuisine": "Asian"
    },
    "Grilled Vegetables": {
        "ingredients": ["Carrot", "Potato", "Onion", "Cucumber", "Olive oil", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Mediterranean"
    },
    "Vegetable Soup": {
        "ingredients": ["Tomato", "Onion", "Carrot", "Potato", "Garlic", "Salt", "Pepper", "Olive oil"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Mediterranean"
    },
    "Grilled Cheese and Tomato Soup": {
        "ingredients": ["Bread", "Cheese", "Tomato", "Onion", "Garlic", "Butter", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["high-protein"],
        "cuisine": "American"
    },
    "Pasta Primavera": {
        "ingredients": ["Pasta", "Tomato", "Garlic", "Carrot", "Olive oil", "Cucumber", "Basil", "Salt", "Pepper"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["vegetarian"],
        "cuisine": "Italian"
    },
    "Cauliflower Rice": {
        "ingredients": ["Cauliflower", "Garlic", "Olive oil", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": ["low-carb", "gluten-free"],
        "cuisine": "Asian"
    },
    "Egg Salad": {
        "ingredients": ["Egg", "Mayonnaise", "Salt", "Pepper", "Onion", "Mustard", "Lettuce"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["high-protein"],
        "cuisine": "American"
    },
    "Stuffed Bell Peppers": {
        "ingredients": ["Bell peppers", "Rice", "Tomato", "Onion", "Cheese", "Ground beef", "Garlic", "Salt", "Pepper"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["comfort-food"],
        "cuisine": "American"
    },
    "Shakshuka": {
        "ingredients": ["Egg", "Tomato", "Onion", "Garlic", "Cumin", "Coriander", "Chili", "Olive oil", "Salt"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["vegetarian"],
        "cuisine": "Middle Eastern"
    },
    "Fruit Salad": {
        "ingredients": ["Banana", "Apple", "Orange", "Grapes", "Honey", "Lemon juice"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based"],
        "cuisine": "American"
    },
    "Mashed Potatoes": {
        "ingredients": ["Potato", "Butter", "Milk", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["comfort-food"],
        "cuisine": "American"
    },
    "Egg Fried Rice": {
        "ingredients": ["Rice", "Egg", "Onion", "Garlic", "Soy sauce", "Peas", "Carrot", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free", "high-protein"],
        "cuisine": "Asian"
    },
    "Tacos": {
        "ingredients": ["Tortilla", "Ground beef", "Lettuce", "Tomato", "Onion", "Cheese", "Sour cream"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["high-protein"],
        "cuisine": "Mexican"
    },
    "Baked Chicken": {
        "ingredients": ["Chicken", "Salt", "Pepper", "Garlic", "Olive oil", "Lemon", "Rosemary"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["high-protein"],
        "cuisine": "American"
    },
    "Vegetable Stir Fry": {
        "ingredients": ["Carrot", "Cucumber", "Onion", "Peas", "Bell pepper", "Soy sauce", "Garlic", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free", "plant-based"],
        "cuisine": "Asian"
    },
    "Chickpea Salad": {
        "ingredients": ["Chickpeas", "Tomato", "Cucumber", "Onion", "Lemon juice", "Olive oil", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Mediterranean"
    },
    "Apple Crumble": {
        "ingredients": ["Apple", "Flour", "Sugar", "Butter", "Cinnamon"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["dessert"],
        "cuisine": "American"
    },
    "Quesadilla": {
        "ingredients": ["Tortilla", "Cheese", "Onion", "Bell pepper", "Oil"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": ["high-protein"],
        "cuisine": "Mexican"
    },
    "Chicken Caesar Salad": {
        "ingredients": ["Chicken", "Lettuce", "Cheese", "Croutons", "Caesar dressing", "Garlic"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["high-protein"],
        "cuisine": "American"
    },
    "Lentil Soup": {
        "ingredients": ["Lentils", "Onion", "Garlic", "Carrot", "Tomato", "Cumin", "Curry powder", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"],
        "cuisine": "Mediterranean"
    }

}


def get_ingredients():
    return ingredients

def get_recipes():
    return recipes