import React from 'react';
import { clsx } from 'clsx';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  className?: string;
}

export const Button: React.FC<ButtonProps> = ({ children, className = '', ...props }) => {
  return (
    <button
      {...props}
      className={clsx(
        'px-4 py-2 rounded-lg font-medium text-sm transition-all duration-200',
        'bg-blue-600 text-white hover:bg-blue-700',
        className
      )}
    >
      {children}
    </button>
  );
};