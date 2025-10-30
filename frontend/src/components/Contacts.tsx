import React from 'react';
import { Download, List, Star } from 'lucide-react';

const Contacts: React.FC = () => {
  return (
    <div className="p-6 space-y-8">
      <h1 className="text-2xl font-semibold text-gray-800">Contacts</h1>

      {/* Top Actions */}
      <div className="grid grid-cols-2 gap-6">
        <div className="border border-gray-200 rounded-xl p-6 bg-white flex items-center justify-between hover:shadow-sm transition-all">
          <div>
            <div className="flex items-center gap-3">
              <Download className="text-blue-600" size={28} />
              <h2 className="text-lg font-semibold text-gray-800">Import CSV</h2>
            </div>
            <p className="text-gray-500 text-sm mt-2 leading-relaxed max-w-md">
              Import your list, edit it, and add enrichment, such as verifying emails and scraping website or LinkedIn data. Once your list is enriched and ready, you can launch a campaign.
            </p>
          </div>
          <Download className="text-blue-600" size={28} />
        </div>

        <div className="border border-gray-200 rounded-xl p-6 bg-white flex items-center justify-between hover:shadow-sm transition-all">
          <div>
            <div className="flex items-center gap-3">
              <List className="text-blue-600" size={28} />
              <h2 className="text-lg font-semibold text-gray-800">Create Blank List</h2>
            </div>
            <p className="text-gray-500 text-sm mt-2 leading-relaxed max-w-md">
              Start with a blank list to add leads and begin your data enrichment process, such as verifying emails, scraping website or LinkedIn data, and using AI to generate personalized lines.
            </p>
          </div>
          <img src="/blank_list_illustration.svg" alt="Create Blank List" className="h-20" />
        </div>
      </div>

      {/* Spread the word */}
      <div className="grid grid-cols-3 gap-6">
        <div className="col-span-2 border border-gray-200 rounded-xl p-6 bg-white">
          <h2 className="text-lg font-semibold text-gray-800 mb-4">Spread the word about plusvibe.ai</h2>
          <div className="grid grid-cols-2 gap-6">
            <div className="bg-yellow-50 border border-yellow-100 rounded-lg p-4">
              <div className="flex items-center gap-2 mb-2">
                <Star className="text-yellow-500" size={20} />
                <p className="font-medium text-gray-800">Write a Review</p>
              </div>
              <p className="text-sm text-gray-600 leading-relaxed mb-4">
                Write a review about us on G2 or publish a post about your experience on Twitter or LinkedIn to help us reach more people.
              </p>
              <button className="border border-blue-500 text-blue-600 px-4 py-2 rounded-md text-sm font-medium hover:bg-blue-50 transition-all">
                Write Review
              </button>
            </div>

            <div className="bg-blue-50 border border-blue-100 rounded-lg p-4">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-blue-500 text-lg">🎁</span>
                <p className="font-medium text-gray-800">Get Rewarded</p>
              </div>
              <p className="text-sm text-gray-600 leading-relaxed">
                Send us a screenshot or a link to your review/post to <span className="font-medium text-blue-600">team@plusvibe.ai</span> or contact support via the intercom widget, and we’ll add a bonus of <span className="font-semibold">1000 Enrichment Credits</span> to your account.
              </p>
            </div>
          </div>
        </div>

        <div className="border border-gray-200 rounded-xl p-6 bg-white">
          <h2 className="text-lg font-semibold text-gray-800 mb-4">Resources</h2>
          <ul className="space-y-4">
            {[
              { title: 'Cold Outreach Academy', desc: 'Learn effective outreach strategies' },
              { title: '30+ List Building Strategies', desc: 'Grow your prospect database' },
              { title: 'Ideal Customer Profile', desc: 'Swipe file templates' },
              { title: 'Cold Email Template Hub', desc: '650+ proven templates' },
              { title: 'Enrichment & Personalization', desc: 'Level up your prospecting' },
            ].map((item, i) => (
              <li key={i} className="flex flex-col">
                <p className="text-sm font-medium text-gray-800">{item.title}</p>
                <span className="text-xs text-gray-500">{item.desc}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Contacts;