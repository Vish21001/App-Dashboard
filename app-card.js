import React from 'react';

export default function AppCard({ app }) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px' }}>
      <h3>{app.name}</h3>
      <p>Category: {app.category}</p>
      <p>Downloads: {app.downloads.toLocaleString()}</p>
      <p>Rating: {app.rating}</p>
      <p>Price: ${app.price}</p>
    </div>
  );
}
