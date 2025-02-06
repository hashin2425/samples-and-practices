import React from 'react';

const Header: React.FC = () => {
    return (
        <header className="bg-blue-500 text-white p-4">
            <div className="container mx-auto">
                <h1 className="text-2xl font-bold">My Application</h1>
            </div>
        </header>
    );
};

export default Header;