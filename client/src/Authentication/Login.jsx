import React, { useState, useContext } from "react";
import AuthContext from "../Context/AuthContext";
import { jwtDecode } from "jwt-decode";
import { useHistory } from "react-router-dom";
import './login.css'

const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  let history = useHistory()

  const {user, setUser, setAuthTokens} = useContext(AuthContext);

  const submit = async (e) => {
    e.preventDefault();

    let response = await fetch("http://localhost:8000/api/token/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    });

    let data = await response.json();

    if (response.status === 200) {
      setAuthTokens(data);
      setUser(jwtDecode(data.access));
      localStorage.setItem('authTokens', JSON.stringify(data))
      history.push('/')
    } else {
      alert("Something went wrong!");
    }
  };

  return (
    <div className="login-div">
      <h2 className="login-h2">Login</h2>
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
            type="password"
            name="password"
            placeholder="Enter Password"
            onChange={(e) => setPassword(e.target.value)}
            className="login-input"
          />
        </div>
        <button type="submit" className="login-button">Login</button>
      </form>
    </div>
  );
};

export default LoginForm;
