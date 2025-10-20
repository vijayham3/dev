import React, { useContext } from 'react';
import { AuthContext } from '../contexts/AuthContext';
import { Link } from 'react-router-dom';

function Navbar() {
  const { user, logoutUser } = useContext(AuthContext);

  return (
    <nav style={{ padding: '10px', borderBottom: '1px solid #ccc' }}>
      <Link to="/">Home</Link>
      {user ? (
        <button onClick={logoutUser} style={{ marginLeft: '20px' }}>
          Logout
        </button>
      ) : (
        <>
          <Link to="/login" style={{ marginLeft: '20px' }}>Login</Link>
          <Link to="/register" style={{ marginLeft: '10px' }}>Register</Link>
        </>
      )}
    </nav>
  );
}

export default Navbar;
