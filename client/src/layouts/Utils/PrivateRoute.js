import { useContext } from 'react';
import { Route, Redirect} from 'react-router-dom'
import AuthContext from '../../Context/AuthContext';

const PrivateRoute = ({children, ...rest}) => {

    const {user} = useContext(AuthContext);

    return(
        <Route {...rest}>{!authenticated ? <Redirect to="/login" /> : children}</Route>
    )
}

export default PrivateRoute;