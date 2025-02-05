import React from "react";

interface HelloWorldProps {
  greeting: string;
}

const HelloWorld: React.FC<HelloWorldProps> = (props) => {
  return (
    <React.Fragment>
      Greeting: {props.greeting}
    </React.Fragment>
  );
};

export default HelloWorld;
