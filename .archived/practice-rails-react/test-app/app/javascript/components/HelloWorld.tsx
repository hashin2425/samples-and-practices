import React from "react";

interface HelloWorldProps {
  greeting: string;
}

const HelloWorld: React.FC<HelloWorldProps> = ({ greeting }) => {
  return <React.Fragment>Greeting: {greeting}</React.Fragment>;
};

export default HelloWorld;
