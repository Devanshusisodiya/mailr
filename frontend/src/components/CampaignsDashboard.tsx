import React from 'react';
import { Card, CardContent } from './ui/card';
import { Button } from './ui/button';
import { Search, MoreVertical } from 'lucide-react';

interface Campaign {
  name: string;
  status: 'Paused' | 'Completed' | 'Draft';
  leads: number;
  contacted: string;
  bounced?: string;
}

const CampaignsDashboard: React.FC = () => {
  const campaigns: Campaign[] = [
    { name: 'Cybersecurity GEO', status: 'Paused', leads: 7058, contacted: '1.9%', bounced: 'Due to high bounce' },
    { name: 'Gambling site', status: 'Paused', leads: 1083, contacted: '39.5%', bounced: 'High bounce' },
    { name: 'Law firm GEO', status: 'Paused', leads: 544, contacted: '23.2%', bounced: 'Due to high bounce' },
    { name: 'Real Estate LinkedIn with changes', status: 'Completed', leads: 586, contacted: '100%' },
    { name: 'Real Estate Instagram', status: 'Completed', leads: 127, contacted: '100%' },
    { name: 'Podcast LinkedIn', status: 'Completed', leads: 800, contacted: '100%' },
    { name: 'Real Estate LinkedIn', status: 'Completed', leads: 719, contacted: '100%' },
    { name: 'Finance Himanshu', status: 'Completed', leads: 573, contacted: '100%' },
    { name: 'Podcast List Nitesh', status: 'Draft', leads: 0, contacted: '0%' },
  ];

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-semibold text-gray-800">Campaigns</h1>
        <Button>+ Add New Campaign</Button>
      </div>

      <div className="grid grid-cols-4 gap-4 mb-8">
        {[
          { label: 'Total Leads', value: '12,649' },
          { label: 'Total Contacted', value: '4,653' },
          { label: 'Finished', value: '32.8%' },
          { label: 'Positive Reply', value: '0.0%' },
        ].map((card, i) => (
          <Card key={i} className="border border-gray-200">
            <CardContent className="text-center">
              <p className="text-gray-500 text-sm">{card.label}</p>
              <p className="text-3xl font-bold text-blue-600">{card.value}</p>
            </CardContent>
          </Card>
        ))}
      </div>

      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center border rounded-lg px-3 py-2 bg-white w-1/2">
          <Search className="text-gray-400 mr-2" size={18} />
          <input
            type="text"
            placeholder="Search by Email name or campaign name"
            className="w-full outline-none text-sm"
          />
        </div>
        <p className="text-gray-500 text-sm">Showing {campaigns.length} campaigns</p>
      </div>

      <div className="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden max-h-[50vh] overflow-y-auto">
        <table className="w-full text-sm">
          <thead className="bg-gray-100 text-gray-600 sticky top-0">
            <tr>
              <th className="text-left p-3">Campaign Name</th>
              <th className="text-left p-3">Status</th>
              <th className="text-center p-3">Leads</th>
              <th className="text-center p-3">Contacted</th>
              <th className="text-center p-3">Remarks</th>
              <th className="text-center p-3">Actions</th>
            </tr>
          </thead>
          <tbody>
            {campaigns.map((c, i) => (
              <tr key={i} className="border-t hover:bg-gray-50">
                <td className="p-3 font-medium text-gray-800">{c.name}</td>
                <td className="p-3">
                  <span
                    className={`px-2 py-1 rounded-full text-xs font-semibold ${
                      c.status === 'Completed'
                        ? 'bg-green-100 text-green-700'
                        : c.status === 'Paused'
                        ? 'bg-red-100 text-red-700'
                        : 'bg-gray-100 text-gray-600'
                    }`}
                  >
                    {c.status}
                  </span>
                </td>
                <td className="text-center p-3 text-gray-700">{c.leads}</td>
                <td className="text-center p-3 text-gray-700">{c.contacted}</td>
                <td className="text-center p-3 text-sm text-red-500">{c.bounced || '-'}</td>
                <td className="text-center p-3">
                  <MoreVertical className="mx-auto text-gray-400 cursor-pointer" size={16} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default CampaignsDashboard;