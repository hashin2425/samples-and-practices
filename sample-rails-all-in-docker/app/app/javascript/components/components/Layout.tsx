import Header from "./Header";
import Footer from "./Footer";
import React from "react";

const Layout: React.FC = ({ children }) => {
  return (
    <div>
      <Header />
      <main className="container mx-auto p-4">{children}</main>
      <Footer />
    </div>
  );
};

export default Layout;