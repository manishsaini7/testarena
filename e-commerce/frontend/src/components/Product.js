// src/components/Product.js
import React from 'react';

function Product({ product }) {
  return (
    <div className="product">
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <p>Price: ₹{product.price}</p>
    </div>
  );
}

export default Product;
