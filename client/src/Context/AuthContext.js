import { createContext, useEffect, useState } from "react";
import { jwtDecode } from "jwt-decode";
import { useHistory } from "react-router-dom";

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {

  let history = useHistory();

  let [user, setUser] = useState(() => localStorage.getItem("authTokens") ? jwtDecode(localStorage.getItem("authTokens")) : null);
  let [authTokens, setAuthTokens] = useState(() => localStorage.getItem("authTokens") ? JSON.parse(localStorage.getItem("authTokens")) : null);
  let [loading, setLoading] = useState(true);

  let logoutUser = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authTokens");
    history.push("/login");
  };

  let updateToken = async () => {
    console.log('update token called!')
    console.log('refresh',authTokens.refresh)
    let response = await fetch("http://localhost:8000/api/token/refresh/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          'refresh': authTokens.refresh
        }),
      });
      let data = await response.json()

      if (response.status === 200) {
        setAuthTokens(data);
        setUser(jwtDecode(data.access));
        localStorage.setItem('authTokens', JSON.stringify(data))
      } else {
        console.log('bad response')
        logoutUser()
      }
  }

  let contextData = {
    user: user,
    setUser: setUser,
    authTokens: authTokens,
    setAuthTokens: setAuthTokens,
    logoutUser: logoutUser,
  };

  useEffect(() => {

    let fourMinutes = 1000 * 60 * 4;
    let interval = setInterval(() => {
        if(authTokens){
            updateToken()
        }
    }, fourMinutes)

    return () => clearInterval(interval)

  }, [authTokens, loading])

  return (
    <AuthContext.Provider value={contextData}>{children}</AuthContext.Provider>
  );
};
