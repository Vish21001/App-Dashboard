import React from 'react';
import { Bar } from 'react-chartjs-2';
import apps from '../data/apps';

export default function Analytics() {
  const categories = [...new Set(apps.map(app => app.category))];
  const downloads = categories.map(cat =>
    apps.filter(app => app.category === cat).reduce((sum, a) => sum + a.downloads, 0)
  );

  const data = {
    labels: categories,
    datasets: [
      {
        label: 'Total Downloads',
        data: downloads,
        backgroundColor: 'rgba(75,192,192,0.6)',
      },
    ],
  };

  return (
    <div style={{ width: '600px', margin: '20px auto' }}>
      <h2>App Downloads by Category</h2>
      <Bar data={data} />
    </div>
  );
}
