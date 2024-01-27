import React, { useState } from "react";

const RegisterForm = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const submit = async (e) => {
    e.preventDefault();

  };

  return (
    <div className="login-div">
      <h2 className="login-h2">Register</h2>
      <form onSubmit={submit} className="login-form">
        <div>
          <input
            type="text"
            name="username"
            placeholder="Enter Username"
            onChange={(e) => setUsername(e.target.value)}
            className="login-input"
          />
        </div>
        <div>
          <input
            type="email"
            name="email"
            placeholder="Enter Email"
            onChange={(e) => setEmail(e.target.value)}
            className="login-input"
          />
        </div>
        <div>
          <input
            type="password"
            name="password"
            placeholder="Enter Password"
            onChange={(e) => setPassword(e.target.value)}
            className="login-input"
          />
        </div>
        <button type="submit" className="login-button">
          Register
        </button>
      </form>
    </div>
  );
};

export default RegisterForm;
