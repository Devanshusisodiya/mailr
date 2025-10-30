import React from 'react';
import { User, Key, Building, Server, Users, Lock } from 'lucide-react';

const Settings: React.FC = () => {
  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <aside className="w-64 border-r bg-gradient-to-b from-white to-gray-50 p-4 flex flex-col">
        <h2 className="text-sm font-semibold text-gray-500 mb-4">Account Settings</h2>
        <ul className="space-y-2 mb-6">
          <li className="flex items-center gap-2 text-blue-600 font-medium bg-blue-50 rounded-md px-3 py-2">
            <User size={16} /> Profile Settings
          </li>
          <li className="flex items-center gap-2 text-gray-600 hover:text-blue-600 hover:bg-gray-100 px-3 py-2 rounded-md cursor-pointer">
            <Building size={16} /> Billing & Usage
          </li>
          <li className="flex items-center gap-2 text-gray-600 hover:text-blue-600 hover:bg-gray-100 px-3 py-2 rounded-md cursor-pointer">
            <Server size={16} /> Workspaces
          </li>
          <li className="flex items-center gap-2 text-gray-600 hover:text-blue-600 hover:bg-gray-100 px-3 py-2 rounded-md cursor-pointer">
            <Key size={16} /> API Access
          </li>
          <li className="flex items-center gap-2 text-gray-600 hover:text-blue-600 hover:bg-gray-100 px-3 py-2 rounded-md cursor-pointer">
            <Users size={16} /> Client Access
          </li>
        </ul>

        <h2 className="text-sm font-semibold text-gray-500 mb-4">Workspace Settings</h2>
        <ul className="space-y-2">
          <li className="flex items-center gap-2 text-gray-600 hover:text-blue-600 hover:bg-gray-100 px-3 py-2 rounded-md cursor-pointer">
            <Users size={16} /> Members
          </li>
          <li className="flex items-center gap-2 text-gray-600 hover:text-blue-600 hover:bg-gray-100 px-3 py-2 rounded-md cursor-pointer">
            <Lock size={16} /> Key Management
          </li>
        </ul>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-8 overflow-y-auto bg-white">
        <h1 className="text-2xl font-semibold text-gray-800 mb-8">Profile Settings</h1>

        {/* Profile Header */}
        <div className="border border-gray-200 rounded-xl bg-gradient-to-r from-gray-50 to-white p-6 flex items-center justify-between mb-8">
          <div className="flex items-center gap-4">
            <div className="w-16 h-16 rounded-full bg-gray-200 flex items-center justify-center text-gray-500 text-xl font-bold">
              JA
            </div>
            <div>
              <p className="font-semibold text-gray-800">Jyotir Anand</p>
              <p className="text-sm text-gray-500">jyotiranand1@gmail.com</p>
            </div>
          </div>
          <button className="border border-blue-500 text-blue-600 px-4 py-2 rounded-md text-sm font-medium hover:bg-blue-50 transition-all">
            Change Profile Photo
          </button>
        </div>

        {/* Account Details */}
        <section className="border border-gray-200 rounded-xl p-6 mb-8">
          <h2 className="text-lg font-semibold text-gray-800 mb-4">Account Details</h2>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <div>
              <label className="block text-sm text-gray-600 mb-1">First Name</label>
              <input
                type="text"
                value="Jyotir"
                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:ring-2 focus:ring-blue-400 outline-none"
              />
            </div>
            <div>
              <label className="block text-sm text-gray-600 mb-1">Last Name</label>
              <input
                type="text"
                value="Anand"
                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:ring-2 focus:ring-blue-400 outline-none"
              />
            </div>
            <div className="col-span-2">
              <label className="block text-sm text-gray-600 mb-1">Email</label>
              <input
                type="email"
                value="jyotiranand1@gmail.com"
                disabled
                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm bg-gray-50 text-gray-500 cursor-not-allowed"
              />
            </div>
          </div>
          <div className="flex gap-3">
            <button className="border border-gray-300 text-gray-600 px-4 py-2 rounded-md text-sm hover:bg-gray-100">Reset</button>
            <button className="bg-blue-600 text-white px-4 py-2 rounded-md text-sm hover:bg-blue-700">Save Changes</button>
          </div>
        </section>

        {/* Change Password */}
        <section className="border border-gray-200 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-gray-800 mb-4">Change Password</h2>
          <div className="border border-blue-100 bg-blue-50 rounded-md p-4 mb-4">
            <p className="text-sm font-medium text-blue-700 mb-1">Password Requirements:</p>
            <ul className="text-sm text-gray-600 list-disc pl-5">
              <li>Must be a minimum of 8 characters long and include at least one number.</li>
            </ul>
          </div>

          <div className="grid grid-cols-3 gap-4">
            <div>
              <label className="block text-sm text-gray-600 mb-1">Current Password</label>
              <input
                type="password"
                placeholder="Current Password"
                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:ring-2 focus:ring-blue-400 outline-none"
              />
            </div>
            <div>
              <label className="block text-sm text-gray-600 mb-1">New Password</label>
              <input
                type="password"
                placeholder="New Password"
                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:ring-2 focus:ring-blue-400 outline-none"
              />
            </div>
            <div>
              <label className="block text-sm text-gray-600 mb-1">Confirm New Password</label>
              <input
                type="password"
                placeholder="Confirm New Password"
                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:ring-2 focus:ring-blue-400 outline-none"
              />
            </div>
          </div>
          <div className="mt-4">
            <button className="bg-blue-600 text-white px-4 py-2 rounded-md text-sm hover:bg-blue-700">Update Password</button>
          </div>
        </section>
      </main>
    </div>
  );
};

export default Settings;