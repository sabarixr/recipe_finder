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
    'Pancake', 'Hummus', 'Mayonnaise', 'Pasta', 'Semolina', 'Mushrooms', 'Sushi rice', 'Mayo', 'Pork bones',
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
        "dietary_compatibility": ["low-carb", "gluten-free"]
    },
    "Omelette": {
        "ingredients": ["Egg", "Cheese", "Onion", "Salt", "Pepper"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based"]
    },
    "Smoothie": {
        "ingredients": ["Milk", "Banana", "Honey", "Yogurt"],
        "difficulty": 1,
        "prep_time": 5,
        "dietary_compatibility": ["plant-based"]
    },
    "Cake": {
        "ingredients": ["Egg", "Milk", "Flour", "Sugar", "Butter"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["low-carb"]
    },
    "Chicken Curry": {
        "ingredients": ["Chicken", "Tomato", "Onion", "Garlic", "Oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"]
    },
    "Guacamole": {
        "ingredients": ["Avocado", "Lime", "Onion", "Salt", "Cilantro"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based", "gluten-free", "low-carb"]
    },
    "Vegetable Stir-Fry": {
        "ingredients": ["Broccoli", "Carrot", "Garlic", "Soy sauce", "Sesame oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Beef Stew": {
        "ingredients": ["Beef", "Carrot", "Onion", "Garlic", "Potato"],
        "difficulty": 4,
        "prep_time": 120,
        "dietary_compatibility": ["gluten-free"]
    },
    "Fish Tacos": {
        "ingredients": ["Fish", "Tortilla", "Cabbage", "Lime", "Cilantro"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Greek Salad": {
        "ingredients": ["Cucumber", "Tomato", "Feta", "Olive oil", "Olives"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based", "gluten-free", "low-carb"]
    },
    "Pad Thai": {
        "ingredients": ["Rice noodles", "Tofu", "Egg", "Fish sauce", "Peanuts"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Tomato Basil Pasta": {
        "ingredients": ["Pasta", "Tomato", "Basil", "Olive oil", "Garlic"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based"]
    },
    "Shakshuka": {
        "ingredients": ["Egg", "Tomato", "Onion", "Garlic", "Bell pepper"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Chana Masala": {
        "ingredients": ["Chickpeas", "Tomato", "Onion", "Garlic", "Cumin"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Falafel": {
        "ingredients": ["Chickpeas", "Garlic", "Cumin", "Cilantro", "Flour"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["plant-based"]
    },
    "Coconut Rice": {
        "ingredients": ["Rice", "Coconut milk", "Salt", "Sugar", "Water"],
        "difficulty": 1,
        "prep_time": 25,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Tacos Al Pastor": {
        "ingredients": ["Pork", "Pineapple", "Tortilla", "Onion", "Cilantro"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": ["gluten-free"]
    },
    "Miso Soup": {
        "ingredients": ["Miso paste", "Tofu", "Seaweed", "Green onion", "Dashi"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Ratatouille": {
        "ingredients": ["Eggplant", "Zucchini", "Tomato", "Onion", "Garlic"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["plant-based", "gluten-free", "low-carb"]
    },
    "Spinach and Ricotta Ravioli": {
        "ingredients": ["Spinach", "Ricotta", "Flour", "Egg", "Parmesan"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": []
    },
    "Fried Rice": {
        "ingredients": ["Rice", "Egg", "Soy sauce", "Garlic", "Onion"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": []
    },
    "Sushi Rolls": {
        "ingredients": ["Rice", "Nori", "Fish", "Cucumber", "Avocado"],
        "difficulty": 3,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Tiramisu": {
        "ingredients": ["Mascarpone", "Egg", "Sugar", "Coffee", "Cocoa powder"],
        "difficulty": 4,
        "prep_time": 120,
        "dietary_compatibility": []
    },
    "Eggplant Parmesan": {
        "ingredients": ["Eggplant", "Tomato sauce", "Mozzarella", "Parmesan", "Basil"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Gazpacho": {
        "ingredients": ["Tomato", "Cucumber", "Bell pepper", "Garlic", "Olive oil"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["plant-based", "gluten-free", "low-carb"]
    },
    "Lamb Kebabs": {
        "ingredients": ["Lamb", "Garlic", "Cumin", "Onion", "Parsley"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["gluten-free"]
    },
    "Pesto Pasta": {
        "ingredients": ["Basil", "Pine nuts", "Parmesan", "Garlic", "Olive oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based"]
    },
    "Biryani": {
        "ingredients": ["Rice", "Chicken", "Yogurt", "Onion", "Spices"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": ["gluten-free"]
    },
    "Spaghetti Bolognese": {
        "ingredients": ["Spaghetti", "Beef", "Tomato", "Onion", "Garlic"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Fried Chicken": {
        "ingredients": ["Chicken", "Flour", "Egg", "Oil", "Salt"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Shrimp Scampi": {
        "ingredients": ["Shrimp", "Garlic", "Butter", "Lemon", "Pasta"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Grilled Cheese Sandwich": {
        "ingredients": ["Bread", "Cheese", "Butter"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": []
    },
    "Caesar Salad": {
        "ingredients": ["Romaine lettuce", "Parmesan", "Croutons", "Caesar dressing"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["low-carb"]
    },
    "Margherita Pizza": {
        "ingredients": ["Pizza dough", "Tomato", "Mozzarella", "Basil"],
        "difficulty": 3,
        "prep_time": 25,
        "dietary_compatibility": []
    },
    "Lasagna": {
        "ingredients": ["Lasagna noodles", "Beef", "Ricotta", "Tomato sauce", "Parmesan"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": []
    },
    "Chicken Alfredo": {
        "ingredients": ["Chicken", "Pasta", "Butter", "Cream", "Parmesan"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Tuna Salad": {
        "ingredients": ["Tuna", "Mayo", "Celery", "Onion", "Salt"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["gluten-free", "low-carb"]
    },
    "French Toast": {
        "ingredients": ["Egg", "Milk", "Bread", "Cinnamon", "Butter"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": []
    },
    "Ramen": {
        "ingredients": ["Ramen noodles", "Egg", "Soy sauce", "Chicken broth", "Green onion"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": []
    },
    "Clam Chowder": {
        "ingredients": ["Clams", "Potato", "Cream", "Onion", "Bacon"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Teriyaki Chicken": {
        "ingredients": ["Chicken", "Soy sauce", "Sugar", "Garlic", "Ginger"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Mac and Cheese": {
        "ingredients": ["Macaroni", "Cheddar", "Butter", "Milk", "Flour"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": []
    },
    "Stuffed Peppers": {
        "ingredients": ["Bell pepper", "Rice", "Beef", "Tomato", "Cheese"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"]
    },
    "Chili": {
        "ingredients": ["Beef", "Kidney beans", "Tomato", "Onion", "Garlic"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["gluten-free"]
    },
    "Potato Salad": {
        "ingredients": ["Potato", "Mayo", "Mustard", "Celery", "Onion"],
        "difficulty": 1,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Chicken Wings": {
        "ingredients": ["Chicken wings", "Hot sauce", "Butter", "Garlic", "Celery"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Lamb Chops": {
        "ingredients": ["Lamb", "Garlic", "Rosemary", "Olive oil", "Salt"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free", "low-carb"]
    },
    "Cobb Salad": {
        "ingredients": ["Lettuce", "Bacon", "Chicken", "Egg", "Avocado"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free", "low-carb"]
    },
    "Quesadilla": {
        "ingredients": ["Tortilla", "Cheese", "Chicken", "Onion", "Bell pepper"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": []
    },
    "Frittata": {
        "ingredients": ["Egg", "Onion", "Potato", "Cheese", "Spinach"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["gluten-free", "low-carb"]
    },
    "Pulled Pork Sandwich": {
        "ingredients": ["Pork", "BBQ sauce", "Bun", "Onion", "Pickle"],
        "difficulty": 4,
        "prep_time": 120,
        "dietary_compatibility": []
    },
    "Burrito": {
        "ingredients": ["Tortilla", "Beef", "Rice", "Cheese", "Beans"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Pho": {
        "ingredients": ["Rice noodles", "Beef", "Ginger", "Garlic", "Star anise"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Crab Cakes": {
        "ingredients": ["Crab", "Breadcrumbs", "Egg", "Mayonnaise", "Dijon mustard"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Egg Salad": {
        "ingredients": ["Egg", "Mayo", "Mustard", "Onion", "Celery"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["gluten-free", "low-carb"]
    },
    "Chicken Parmesan": {
        "ingredients": ["Chicken", "Parmesan", "Breadcrumbs", "Tomato sauce", "Mozzarella"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Minestrone": {
        "ingredients": ["Pasta", "Tomato", "Carrot", "Onion", "Beans"],
        "difficulty": 2,
        "prep_time": 35,
        "dietary_compatibility": []
    },
    "Pesto Chicken": {
        "ingredients": ["Chicken", "Basil", "Pine nuts", "Garlic", "Parmesan"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free", "low-carb"]
    },
    "French Onion Soup": {
        "ingredients": ["Onion", "Beef broth", "Cheese", "Bread", "Butter"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Eggplant Stir-Fry": {
        "ingredients": ["Eggplant", "Soy sauce", "Garlic", "Ginger", "Sesame oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Shepherd's Pie": {
        "ingredients": ["Beef", "Potato", "Carrot", "Onion", "Peas"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Cornbread": {
        "ingredients": ["Cornmeal", "Flour", "Egg", "Milk", "Butter"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": []
    },
    "Falafel Wrap": {
        "ingredients": ["Falafel", "Tortilla", "Lettuce", "Tomato", "Hummus"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based"]
    },
    "Chicken Shawarma": {
        "ingredients": ["Chicken", "Garlic", "Yogurt", "Cumin", "Paprika"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"]
    },
    "Chicken Caesar Wrap": {
        "ingredients": ["Tortilla", "Chicken", "Caesar dressing", "Lettuce", "Parmesan"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": []
    },
    "Tuna Melt": {
        "ingredients": ["Tuna", "Cheese", "Bread", "Mayo", "Onion"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": []
    },
    "Sloppy Joes": {
        "ingredients": ["Beef", "Tomato sauce", "Bun", "Onion", "Mustard"],
        "difficulty": 3,
        "prep_time": 25,
        "dietary_compatibility": []
    },
    "Pork Tacos": {
        "ingredients": ["Pork", "Tortilla", "Onion", "Cilantro", "Salsa"],
        "difficulty": 3,
        "prep_time": 35,
        "dietary_compatibility": ["gluten-free"]
    },
    "Broccoli Cheddar Soup": {
        "ingredients": ["Broccoli", "Cheddar", "Cream", "Butter", "Onion"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Chicken Fajitas": {
        "ingredients": ["Chicken", "Bell pepper", "Onion", "Tortilla", "Sour cream"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Caprese Salad": {
        "ingredients": ["Tomato", "Mozzarella", "Basil", "Olive oil", "Balsamic vinegar"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["gluten-free", "low-carb"]
    },
    "Pancit": {
        "ingredients": ["Rice noodles", "Chicken", "Cabbage", "Carrot", "Soy sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Pork Schnitzel": {
        "ingredients": ["Pork", "Breadcrumbs", "Egg", "Flour", "Lemon"],
        "difficulty": 3,
        "prep_time": 25,
        "dietary_compatibility": []
    },
    "Chicken Pot Pie": {
        "ingredients": ["Chicken", "Carrot", "Onion", "Flour", "Butter"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": []
    },
    "Shrimp Fried Rice": {
        "ingredients": ["Shrimp", "Rice", "Egg", "Soy sauce", "Onion"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": []
    },
    "Pad Thai": {
        "ingredients": ["Rice noodles", "Shrimp", "Egg", "Peanut", "Bean sprouts", "Fish sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Sushi Rolls": {
        "ingredients": ["Sushi rice", "Nori", "Tuna", "Avocado", "Cucumber", "Soy sauce"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Beef Bulgogi": {
        "ingredients": ["Beef", "Soy sauce", "Garlic", "Onion", "Sesame oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": []
    },
    "Pho Ga (Chicken Pho)": {
        "ingredients": ["Chicken", "Rice noodles", "Ginger", "Star anise", "Cilantro"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Miso Soup": {
        "ingredients": ["Miso paste", "Tofu", "Seaweed", "Green onion", "Dashi broth"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Kung Pao Chicken": {
        "ingredients": ["Chicken", "Soy sauce", "Peanut", "Bell pepper", "Chili pepper"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Tacos al Pastor": {
        "ingredients": ["Pork", "Tortilla", "Pineapple", "Onion", "Cilantro"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["gluten-free"]
    },
    "Chilaquiles": {
        "ingredients": ["Tortilla chips", "Egg", "Salsa", "Cheese", "Onion"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["gluten-free"]
    },
    "Pozole": {
        "ingredients": ["Pork", "Hominy", "Chili pepper", "Onion", "Cabbage"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": ["gluten-free"]
    },
    "Tamales": {
        "ingredients": ["Corn husks", "Masa harina", "Pork", "Chili pepper", "Cheese"],
        "difficulty": 5,
        "prep_time": 180,
        "dietary_compatibility": ["gluten-free"]
    },
    "Bibimbap": {
        "ingredients": ["Rice", "Beef", "Egg", "Spinach", "Carrot", "Gochujang"],
        "difficulty": 4,
        "prep_time": 50,
        "dietary_compatibility": ["gluten-free"]
    },
    "Chicken Katsu": {
        "ingredients": ["Chicken", "Panko", "Egg", "Flour", "Cabbage"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Thai Green Curry": {
        "ingredients": ["Coconut milk", "Chicken", "Green curry paste", "Basil", "Lime leaves"],
        "difficulty": 4,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"]
    },
    "Banh Mi": {
        "ingredients": ["Baguette", "Pork", "Pickled vegetables", "Cucumber", "Cilantro"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Teriyaki Salmon": {
        "ingredients": ["Salmon", "Soy sauce", "Sugar", "Garlic", "Ginger"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Sesame Chicken": {
        "ingredients": ["Chicken", "Soy sauce", "Sesame oil", "Honey", "Sesame seeds"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Roti Canai": {
        "ingredients": ["Flour", "Butter", "Milk", "Curry sauce"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": []
    },
    "Enchiladas Verdes": {
        "ingredients": ["Tortilla", "Chicken", "Green salsa", "Cheese", "Sour cream"],
        "difficulty": 3,
        "prep_time": 35,
        "dietary_compatibility": ["gluten-free"]
    },
    "Korean Kimchi Stew (Kimchi Jjigae)": {
        "ingredients": ["Kimchi", "Pork belly", "Tofu", "Onion", "Gochujang"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"]
    },
    "Yakitori (Grilled Chicken Skewers)": {
        "ingredients": ["Chicken", "Soy sauce", "Sake", "Sugar", "Green onion"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["gluten-free"]
    },
    "Tonkotsu Ramen": {
        "ingredients": ["Pork bones", "Ramen noodles", "Egg", "Soy sauce", "Green onion"],
        "difficulty": 5,
        "prep_time": 180,
        "dietary_compatibility": []
    },
    "Vietnamese Spring Rolls": {
        "ingredients": ["Rice paper", "Shrimp", "Mint", "Cucumber", "Vermicelli"],
        "difficulty": 3,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Moo Shu Pork": {
        "ingredients": ["Pork", "Egg", "Cabbage", "Mushrooms", "Hoisin sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Mexican Street Tacos": {
        "ingredients": ["Corn tortilla", "Beef", "Onion", "Cilantro", "Lime"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Gyoza (Japanese Dumplings)": {
        "ingredients": ["Pork", "Cabbage", "Garlic", "Ginger", "Dumpling wrappers"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Bibingka (Filipino Rice Cake)": {
        "ingredients": ["Rice flour", "Coconut milk", "Sugar", "Egg", "Butter"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Khao Pad (Thai Fried Rice)": {
        "ingredients": ["Rice", "Egg", "Garlic", "Soy sauce", "Shrimp"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": []
    },
    "Tlayuda (Oaxacan Pizza)": {
        "ingredients": ["Tortilla", "Black beans", "Oaxaca cheese", "Avocado", "Cilantro"],
        "difficulty": 3,
        "prep_time": 35,
        "dietary_compatibility": ["gluten-free"]
    },
    "Chinese Hot Pot": {
        "ingredients": ["Beef", "Tofu", "Mushrooms", "Bok choy", "Broth"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Vietnamese Pho Bo (Beef Pho)": {
        "ingredients": ["Beef", "Rice noodles", "Cinnamon", "Star anise", "Cilantro"],
        "difficulty": 5,
        "prep_time": 120,
        "dietary_compatibility": ["gluten-free"]
    },
    "Tamago Sushi (Egg Sushi)": {
        "ingredients": ["Egg", "Sushi rice", "Nori", "Soy sauce"],
        "difficulty": 3,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Elote (Mexican Street Corn)": {
        "ingredients": ["Corn", "Mayonnaise", "Chili powder", "Lime", "Cheese"],
        "difficulty": 1,
        "prep_time": 15,
        "dietary_compatibility": ["gluten-free"]
    },
    "Banh Bao (Vietnamese Steamed Buns)": {
        "ingredients": ["Flour", "Pork", "Mushrooms", "Egg", "Coriander"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": []
    },
    "Fish Tacos": {
        "ingredients": ["Fish", "Tortilla", "Cabbage", "Lime", "Avocado"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Beef Tacos": {
        "ingredients": ["Beef", "Tortilla", "Cheese", "Sour cream", "Lettuce"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": ["gluten-free"]
    },
    "Kung Pao Shrimp": {
        "ingredients": ["Shrimp", "Peanuts", "Bell pepper", "Soy sauce", "Chili pepper"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Mole Poblano": {
        "ingredients": ["Chicken", "Chili pepper", "Tomato", "Chocolate", "Garlic"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": []
    },
    "Chow Mein": {
        "ingredients": ["Noodles", "Chicken", "Cabbage", "Carrot", "Soy sauce"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": []
    },
    "Spring Rolls": {
        "ingredients": ["Rice paper", "Shrimp", "Cabbage", "Carrot", "Mint"],
        "difficulty": 3,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Carnitas": {
        "ingredients": ["Pork", "Onion", "Cilantro", "Lime", "Salsa"],
        "difficulty": 4,
        "prep_time": 150,
        "dietary_compatibility": ["gluten-free"]
    },
    "Ramen": {
        "ingredients": ["Ramen noodles", "Broth", "Egg", "Soy sauce", "Bok choy"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": []
    },
    "Guacamole": {
        "ingredients": ["Avocado", "Tomato", "Onion", "Cilantro", "Lime"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["gluten-free"]
    },
    "Tteokbokki": {
        "ingredients": ["Rice cakes", "Gojujang", "Fish cakes", "Onion", "Egg"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Samosas": {
        "ingredients": ["Potato", "Peas", "Curry powder", "Flour", "Onion"],
        "difficulty": 3,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Chili Con Carne": {
        "ingredients": ["Beef", "Chili powder", "Tomato", "Beans", "Onion"],
        "difficulty": 3,
        "prep_time": 50,
        "dietary_compatibility": []
    },
    "Peking Duck": {
        "ingredients": ["Duck", "Soy sauce", "Hoisin sauce", "Spring onion", "Pancake"],
        "difficulty": 5,
        "prep_time": 180,
        "dietary_compatibility": []
    },
    "Pho": {
        "ingredients": ["Beef", "Rice noodles", "Ginger", "Cinnamon", "Cloves"],
        "difficulty": 5,
        "prep_time": 120,
        "dietary_compatibility": ["gluten-free"]
    },
    "Quesadilla": {
        "ingredients": ["Tortilla", "Cheese", "Chicken", "Bell pepper", "Onion"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": []
    },
    "Peking Duck Pancakes": {
        "ingredients": ["Duck", "Cucumber", "Spring onion", "Hoisin sauce", "Pancake"],
        "difficulty": 5,
        "prep_time": 180,
        "dietary_compatibility": []
    },
    "Sichuan Hot Pot": {
        "ingredients": ["Beef", "Tofu", "Cabbage", "Chili oil", "Mushrooms"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Bibimbap": {
        "ingredients": ["Rice", "Beef", "Egg", "Spinach", "Carrot", "Gochujang"],
        "difficulty": 4,
        "prep_time": 50,
        "dietary_compatibility": ["gluten-free"]
    },
    "Nasi Goreng": {
        "ingredients": ["Rice", "Egg", "Chicken", "Carrot", "Soy sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Tom Yum Soup": {
        "ingredients": ["Shrimp", "Lemongrass", "Lime leaves", "Chili", "Fish sauce"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Burritos": {
        "ingredients": ["Tortilla", "Beef", "Rice", "Cheese", "Sour cream"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": []
    },
    "Fajitas": {
        "ingredients": ["Chicken", "Bell pepper", "Onion", "Tortilla", "Lime"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Pork Adobo": {
        "ingredients": ["Pork", "Soy sauce", "Vinegar", "Garlic", "Bay leaves"],
        "difficulty": 3,
        "prep_time": 60,
        "dietary_compatibility": []
    },
    "Gado-Gado": {
        "ingredients": ["Tofu", "Cabbage", "Peanut sauce", "Carrot", "Egg"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based"]
    },
    "Kimchi": {
        "ingredients": ["Napa cabbage", "Garlic", "Ginger", "Chili flakes", "Fish sauce"],
        "difficulty": 4,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based"]
    },
    "Dim Sum": {
        "ingredients": ["Pork", "Shrimp", "Dumpling wrappers", "Ginger", "Soy sauce"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": []
    },
    "Churros": {
        "ingredients": ["Flour", "Sugar", "Egg", "Butter", "Cinnamon"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": []
    },
    "Arroz con Pollo": {
        "ingredients": ["Chicken", "Rice", "Tomato", "Garlic", "Peas"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Ceviche": {
        "ingredients": ["Fish", "Lime", "Tomato", "Cilantro", "Onion"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": ["gluten-free"]
    },
    "Dosa": {
        "ingredients": ["Rice", "Flour", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 90,
        "dietary_compatibility": ["gluten-free"]
    },
    "Sambar": {
        "ingredients": ["Lentils", "Tomato", "Onion", "Garlic", "Carrot", "Tamarind", "Coriander", "Curry leaves"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Idli": {
        "ingredients": ["Rice", "Flour", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 120,
        "dietary_compatibility": ["gluten-free"]
    },
    "Vada": {
        "ingredients": ["Lentils", "Onion", "Coriander", "Curry leaves", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["gluten-free"]
    },
    "Upma": {
        "ingredients": ["Semolina", "Onion", "Carrot", "Peas", "Curry leaves", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Pongal": {
        "ingredients": ["Rice", "Lentils", "Pepper", "Ginger", "Curry leaves", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Masala Dosa": {
        "ingredients": ["Rice", "Flour", "Salt", "Oil", "Potato", "Onion", "Mustard seeds", "Curry leaves"],
        "difficulty": 3,
        "prep_time": 120,
        "dietary_compatibility": ["gluten-free"]
    },
    "Avial": {
        "ingredients": ["Carrot", "Potato", "Pumpkin", "Green beans", "Coconut", "Curry leaves", "Tamarind", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Rasam": {
        "ingredients": ["Tomato", "Garlic", "Tamarind", "Coriander", "Curry leaves", "Pepper", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Coconut Chutney": {
        "ingredients": ["Coconut", "Green chili", "Coriander", "Salt", "Oil", "Mustard seeds", "Curry leaves"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Mysore Pak": {
        "ingredients": ["Gram flour", "Sugar", "Butter", "Oil"],
        "difficulty": 4,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Kootu": {
        "ingredients": ["Lentils", "Carrot", "Pumpkin", "Coconut", "Curry leaves", "Chili", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Bisi Bele Bath": {
        "ingredients": ["Rice", "Lentils", "Carrot", "Tomato", "Tamarind", "Curry leaves", "Mustard seeds", "Ginger", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["gluten-free"]
    },
    "Kadhi": {
        "ingredients": ["Yogurt", "Chili", "Curry leaves", "Mustard seeds", "Garlic", "Turmeric", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Chole Bhature": {
        "ingredients": ["Flour", "Chickpeas", "Onion", "Tomato", "Garlic", "Coriander", "Curry leaves", "Salt", "Oil"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": []
    },
    "Chettinad Chicken Curry": {
        "ingredients": ["Chicken", "Tomato", "Onion", "Garlic", "Coriander", "Chili", "Ginger", "Oil"],
        "difficulty": 4,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Curd Rice": {
        "ingredients": ["Rice", "Yogurt", "Curry leaves", "Mustard seeds", "Ginger", "Coriander", "Salt"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Thoran (Cabbage Stir-fry)": {
        "ingredients": ["Cabbage", "Coconut", "Green chili", "Garlic", "Curry leaves", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Paneer Butter Masala": {
        "ingredients": ["Paneer", "Tomato", "Onion", "Garlic", "Butter", "Cream", "Coriander", "Cumin", "Ginger"],
        "difficulty": 4,
        "prep_time": 40,
        "dietary_compatibility": []
    },
    "Aloo Gobi": {
        "ingredients": ["Potato", "Cauliflower", "Onion", "Cumin", "Turmeric", "Coriander", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Pulao": {
        "ingredients": ["Rice", "Carrot", "Peas", "Onion", "Ginger", "Cinnamon", "Cloves", "Cumin", "Salt", "Oil"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["gluten-free"]
    },
    "Baingan Bharta": {
        "ingredients": ["Eggplant", "Onion", "Tomato", "Garlic", "Coriander", "Cumin", "Turmeric", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Chicken Tikka Masala": {
        "ingredients": ["Chicken", "Tomato", "Onion", "Garlic", "Cream", "Ginger", "Cumin", "Coriander", "Chili"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_compatibility": []
    },
    "Pav Bhaji": {
        "ingredients": ["Potato", "Onion", "Tomato", "Cabbage", "Green peas", "Butter", "Coriander", "Bread"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Chana Masala": {
        "ingredients": ["Chickpeas", "Onion", "Tomato", "Garlic", "Cumin", "Coriander", "Turmeric", "Chili", "Salt", "Oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Tandoori Chicken": {
        "ingredients": ["Chicken", "Yogurt", "Ginger", "Garlic", "Cumin", "Chili", "Coriander", "Lemon"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": []
    },
    "Kadhi Pakora": {
        "ingredients": ["Yogurt", "Chickpea flour", "Cumin", "Chili", "Onion", "Garlic", "Turmeric", "Salt", "Oil"],
        "difficulty": 4,
        "prep_time": 50,
        "dietary_compatibility": []
    },
    "Dhokla": {
        "ingredients": ["Gram flour", "Yogurt", "Turmeric", "Cumin", "Curry leaves", "Mustard seeds", "Salt"],
        "difficulty": 3,
        "prep_time": 60,
        "dietary_compatibility": ["gluten-free"]
    },
    "Pav Bhaji": {
        "ingredients": ["Potato", "Onion", "Tomato", "Cabbage", "Green peas", "Butter", "Coriander", "Bread"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Mac and Cheese": {
        "ingredients": ["Macaroni", "Cheese", "Milk", "Butter", "Flour", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": []
    },
    "Cheeseburger": {
        "ingredients": ["Beef", "Cheese", "Bun", "Lettuce", "Tomato", "Onion", "Pickles"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Apple Pie": {
        "ingredients": ["Apple", "Flour", "Sugar", "Butter", "Cinnamon", "Lemon juice"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": []
    },
    "Buffalo Wings": {
        "ingredients": ["Chicken wings", "Hot sauce", "Butter", "Garlic", "Vinegar", "Cayenne pepper"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Clam Chowder": {
        "ingredients": ["Clams", "Potato", "Onion", "Celery", "Milk", "Butter", "Flour", "Parsley"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_compatibility": []
    },
    "Grilled Cheese Sandwich": {
        "ingredients": ["Bread", "Cheese", "Butter"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": []
    },
    "Pulled Pork Sandwich": {
        "ingredients": ["Pork", "Bun", "Barbecue sauce", "Cabbage", "Pickles"],
        "difficulty": 3,
        "prep_time": 120,
        "dietary_compatibility": []
    },
    "Tater Tot Casserole": {
        "ingredients": ["Ground beef", "Tater tots", "Cheese", "Onion", "Cream of mushroom soup"],
        "difficulty": 3,
        "prep_time": 60,
        "dietary_compatibility": []
    },
    "Sloppy Joes": {
        "ingredients": ["Ground beef", "Tomato", "Onion", "Ketchup", "Bread", "Mustard", "Brown sugar"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Pumpkin Pie": {
        "ingredients": ["Pumpkin", "Sugar", "Flour", "Butter", "Egg", "Cinnamon", "Nutmeg"],
        "difficulty": 4,
        "prep_time": 90,
        "dietary_compatibility": []
    },
    "Cornbread": {
        "ingredients": ["Cornmeal", "Flour", "Sugar", "Butter", "Egg", "Milk", "Baking powder"],
        "difficulty": 2,
        "prep_time": 40,
        "dietary_compatibility": []
    },
    "BLT Sandwich": {
        "ingredients": ["Bacon", "Lettuce", "Tomato", "Bread", "Mayonnaise"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": []
    },
    "Fried Rice": {
        "ingredients": ["Rice", "Egg", "Onion", "Garlic", "Soy sauce", "Peas", "Carrot", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Grilled Vegetables": {
        "ingredients": ["Carrot", "Potato", "Onion", "Cucumber", "Olive oil", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Vegetable Soup": {
        "ingredients": ["Tomato", "Onion", "Carrot", "Potato", "Garlic", "Salt", "Pepper", "Olive oil"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Grilled Cheese and Tomato Soup": {
        "ingredients": ["Bread", "Cheese", "Tomato", "Onion", "Garlic", "Butter", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Pasta Primavera": {
        "ingredients": ["Pasta", "Tomato", "Garlic", "Carrot", "Olive oil", "Cucumber", "Basil", "Salt", "Pepper"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Cauliflower Rice": {
        "ingredients": ["Cauliflower", "Garlic", "Olive oil", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": ["low-carb", "gluten-free"]
    },
    "Egg Salad": {
        "ingredients": ["Egg", "Mayonnaise", "Salt", "Pepper", "Onion", "Mustard", "Lettuce"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": []
    },
    "Stuffed Bell Peppers": {
        "ingredients": ["Bell peppers", "Rice", "Tomato", "Onion", "Cheese", "Ground beef", "Garlic", "Salt", "Pepper"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Shakshuka": {
        "ingredients": ["Egg", "Tomato", "Onion", "Garlic", "Cumin", "Coriander", "Chili", "Olive oil", "Salt"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based"]
    },
    "Pancakes": {
        "ingredients": ["Flour", "Egg", "Milk", "Sugar", "Butter", "Baking powder", "Salt"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": []
    },
    "Fruit Salad": {
        "ingredients": ["Banana", "Apple", "Orange", "Grapes", "Honey", "Lemon juice"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_compatibility": ["plant-based"]
    },
    "Mashed Potatoes": {
        "ingredients": ["Potato", "Butter", "Milk", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": []
    },
    "Egg Fried Rice": {
        "ingredients": ["Rice", "Egg", "Onion", "Garlic", "Soy sauce", "Peas", "Carrot", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Tacos": {
        "ingredients": ["Tortilla", "Ground beef", "Lettuce", "Tomato", "Onion", "Cheese", "Sour cream"],
        "difficulty": 3,
        "prep_time": 30,
        "dietary_compatibility": []
    },
    "Baked Chicken": {
        "ingredients": ["Chicken", "Salt", "Pepper", "Garlic", "Olive oil", "Lemon", "Rosemary"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Vegetable Stir Fry": {
        "ingredients": ["Carrot", "Cucumber", "Onion", "Peas", "Bell pepper", "Soy sauce", "Garlic", "Oil"],
        "difficulty": 2,
        "prep_time": 20,
        "dietary_compatibility": ["gluten-free"]
    },
    "Chickpea Salad": {
        "ingredients": ["Chickpeas", "Tomato", "Cucumber", "Onion", "Lemon juice", "Olive oil", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    },
    "Apple Crumble": {
        "ingredients": ["Apple", "Flour", "Sugar", "Butter", "Cinnamon"],
        "difficulty": 3,
        "prep_time": 45,
        "dietary_compatibility": []
    },
    "Quesadilla": {
        "ingredients": ["Tortilla", "Cheese", "Onion", "Bell pepper", "Oil"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_compatibility": []
    },
    "Chicken Caesar Salad": {
        "ingredients": ["Chicken", "Lettuce", "Cheese", "Croutons", "Caesar dressing", "Garlic"],
        "difficulty": 2,
        "prep_time": 25,
        "dietary_compatibility": []
    },
    "Lentil Soup": {
        "ingredients": ["Lentils", "Onion", "Garlic", "Carrot", "Tomato", "Cumin", "Curry powder", "Salt", "Pepper"],
        "difficulty": 2,
        "prep_time": 30,
        "dietary_compatibility": ["plant-based", "gluten-free"]
    }
}


def get_ingredients():
    return ingredients

def get_recipes():
    return recipes