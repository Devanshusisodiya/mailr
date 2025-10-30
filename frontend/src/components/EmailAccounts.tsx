import React from 'react';
import { Mail, Globe, Thermometer, AlertTriangle, Plus, Search } from 'lucide-react';

const emailAccounts = [
  { email: 'jordansanders@waoutbound.info', status: 'Error', health: '97.5%', sent: '0/30', replies: 'N/A', warmup: '0/17' },
  { email: 'amberhayes@waoutbound.info', status: 'Error', health: '100.0%', sent: '0/30', replies: 'N/A', warmup: '0/17' },
  { email: 'allisongriffin@waoutbound.info', status: 'Error', health: '97.6%', sent: '0/30', replies: '0.0%', warmup: '0/17' },
  { email: 'erinrussell@waoutbound.info', status: 'Error', health: '95.3%', sent: '0/30', replies: '0.0%', warmup: '0/17' },
];

const EmailAccounts: React.FC = () => {
  return (
    <div className="p-6 space-y-8">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-semibold text-gray-800">Email Accounts</h1>
        <button className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-all">
          <Plus size={18} /> Add New Account
        </button>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-5 gap-4">
        {[
          { label: 'Total', value: 55, icon: <Mail className="text-blue-600" size={22} /> },
          { label: 'Total Domains', value: 13, icon: <Globe className="text-blue-600" size={22} /> },
          { label: 'Warmup', value: 0, icon: <Thermometer className="text-blue-600" size={22} /> },
          { label: 'Error', value: 39, icon: <AlertTriangle className="text-red-500" size={22} /> },
          { label: 'Alert', value: 0, icon: <AlertTriangle className="text-yellow-500" size={22} /> },
        ].map((item, idx) => (
          <div
            key={idx}
            className="border border-gray-200 rounded-xl p-4 bg-white flex items-center justify-between hover:shadow-sm transition-all"
          >
            <div>
              <p className="text-sm text-gray-500">{item.label}</p>
              <p className="text-2xl font-semibold text-gray-800">{item.value}</p>
            </div>
            {item.icon}
          </div>
        ))}
      </div>

      {/* Search and Filters */}
      <div className="flex justify-between items-center mt-4">
        <div className="flex items-center border border-gray-200 bg-white rounded-lg px-3 py-2 w-1/2">
          <Search className="text-gray-400 mr-2" size={18} />
          <input
            type="text"
            placeholder="Search by account address, first name or campaign name"
            className="w-full outline-none text-sm text-gray-700"
          />
        </div>

        <div className="flex gap-2">
          <select className="border border-gray-200 rounded-md text-sm px-3 py-2 bg-white text-gray-600">
            <option>Warmup Status</option>
          </select>
          <select className="border border-gray-200 rounded-md text-sm px-3 py-2 bg-white text-gray-600">
            <option>Account Status</option>
          </select>
        </div>
      </div>

      {/* Table */}
      <div className="bg-white border border-gray-200 rounded-xl overflow-hidden shadow-sm">
        <table className="w-full text-sm">
          <thead className="bg-gray-50 text-gray-600">
            <tr>
              <th className="p-3 text-left"><input type="checkbox" /></th>
              <th className="p-3 text-left">Account</th>
              <th className="p-3 text-center">Status</th>
              <th className="p-3 text-center">Sent</th>
              <th className="p-3 text-center">Warmup</th>
              <th className="p-3 text-center">Health</th>
              <th className="p-3 text-center">Replies</th>
              <th className="p-3 text-center">Volume</th>
            </tr>
          </thead>
          <tbody>
            {emailAccounts.map((acc, i) => (
              <tr key={i} className="border-t hover:bg-gray-50">
                <td className="p-3"><input type="checkbox" /></td>
                <td className="p-3 text-gray-800">{acc.email}</td>
                <td className="p-3 text-center">
                  <span className="text-red-500 bg-red-50 border border-red-100 rounded-md px-2 py-1 text-xs font-medium">{acc.status}</span>
                </td>
                <td className="p-3 text-center text-gray-600">{acc.sent}</td>
                <td className="p-3 text-center text-gray-600">{acc.warmup}</td>
                <td className="p-3 text-center text-gray-600">{acc.health}</td>
                <td className="p-3 text-center text-gray-600">{acc.replies}</td>
                <td className="p-3 text-center text-gray-600">1</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default EmailAccounts;