import React, { useState } from 'react';
import { GlobalSidebar } from './components/GlobalSidebar';
import CampaignsDashboard from './components/CampaignsDashboard';
import Contacts from './components/Contacts';
import EmailAccounts from './components/EmailAccounts';
import Settings from './components/Settings';

const App: React.FC = () => {
  const [activePage, setActivePage] = useState('campaigns');

  const renderPage = () => {
    switch (activePage) {
      case 'contacts':
        return <Contacts />;
      case 'email':
        return <EmailAccounts />;
      case 'settings':
        return <Settings />;
      case 'campaigns':
      default:
        return <CampaignsDashboard />;
    }
  };

  return (
    <div className="flex min-h-screen bg-gray-50">
      <GlobalSidebar active={activePage} onNavigate={setActivePage} />
      <div className="flex-1 overflow-y-auto">{renderPage()}</div>
    </div>
  );
};

export default App;