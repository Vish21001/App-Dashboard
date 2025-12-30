import React from 'react';
import AppCard from './AppCard';
import apps from '../data/apps';

export default function AppList() {
  return (
    <div>
      <h2>All Apps</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        {apps.map((app) => (
          <AppCard key={app.id} app={app} />
        ))}
      </div>
    </div>
  );
}
