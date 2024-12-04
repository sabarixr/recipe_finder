# Vite + React + Tailwind CSS Boilerplate

This repository is a boilerplate for a React application initialized with Vite and Tailwind CSS. It provides a basic setup to quickly start developing with these technologies.

## Features

- **React**: A JavaScript library for building user interfaces.
- **Vite**: A fast build tool that significantly improves the frontend development experience.
- **Tailwind CSS**: A utility-first CSS framework for rapid UI development.

## Getting Started

Follow these steps to get started with this boilerplate:

### Prerequisites

Make sure you have the following installed:

- Node.js (version 14.0.0 or later)
- npm (version 6.0.0 or later)

### Installation

1. Clone the repository:
    ```git clone https://github.com/sabarixr/react-vite-tailwind-boilerplate.git
    cd react-vite-tailwind-boilerplate
    ```

2. Install dependencies:
    ```
    npm install
    ```

3. Run the development server:
    ```
    npm run dev
    ```

### Folder Structure

```
my-app/
├── node_modules/
├── public/
│   └── vite.svg
├── src/
│   ├── App.jsx
│   ├── index.css
│   ├── main.jsx
│   └── assets/
├── .gitignore
├── index.html
├── package.json
├── postcss.config.js
├── tailwind.config.js
└── vite.config.js
```

### Configuration

- Tailwind CSS: Configuration for Tailwind CSS is in the tailwind.config.js file. Tailwind's utility classes are included in the src/index.css file.

### Usage

Modify the src/App.jsx file to start building your application. Use Tailwind's utility classes to style your components.

### Example

The boilerplate includes a simple example component styled with Tailwind CSS:
```
function App() {
return (
 <div className="min-h-screen flex items-center justify-center bg-gray-100">
   <h1 className="text-3xl font-bold text-blue-600">
     Hello, Tailwind CSS with Vite!
   </h1>
 </div>
);
}

export default App;
```
## Contributing

Feel free to open issues or submit pull requests to improve this boilerplate.


