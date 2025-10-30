import React, { useState } from 'react';
import { Mail, Users, Settings, Send } from 'lucide-react';
import { clsx } from 'clsx';

interface SidebarProps {
  active?: string;
  onNavigate: (page: string) => void;
}

const menuItems = [
  { id: 'campaigns', icon: Mail, label: 'Campaigns' },
  { id: 'contacts', icon: Users, label: 'Contacts' },
  { id: 'email', icon: Send, label: 'Emails' },
  { id: 'settings', icon: Settings, label: 'Settings' },
];

export const GlobalSidebar: React.FC<SidebarProps> = ({ active, onNavigate }) => {
  const [current, setCurrent] = useState(active || 'campaigns');

  const handleClick = (id: string) => {
    setCurrent(id);
    onNavigate(id);
  };

  return (
    <aside className="w-16 h-screen bg-gradient-to-b from-white to-gray-50 border-r flex flex-col items-center py-6 shadow-sm">
      {/* Logo */}
      <div className="flex flex-col items-center mb-8">
        <img src="/assets/sendroq_logo.png" alt="sendroq" className="h-8 mb-6 select-none" />
      </div>

      {/* Menu Icons */}
      <div className="flex flex-col space-y-6 mt-4">
        {menuItems.map((item) => {
          const Icon = item.icon;
          return (
            <button
              key={item.id}
              onClick={() => handleClick(item.id)}
              className={clsx(
                'p-2 rounded-lg transition-all',
                current === item.id
                  ? 'text-blue-600 bg-blue-50'
                  : 'text-gray-700 hover:text-blue-600 hover:bg-gray-100'
              )}
            >
              <Icon size={22} />
            </button>
          );
        })}
      </div>
    </aside>
  );
};
