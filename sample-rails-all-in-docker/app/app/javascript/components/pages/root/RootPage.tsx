import React from "react";
import Layout from "../../components/Layout";

interface RootPageProps {
  greeting: string;
}

const RootPage: React.FC<RootPageProps> = (props) => {
  return (
    <React.Fragment>
        {props.greeting}
    </React.Fragment>
  );
};

export default RootPage;
