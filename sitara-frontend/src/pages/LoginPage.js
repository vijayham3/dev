import React, { useState, useContext } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../contexts/AuthContext';

function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { loginUser } = useContext(AuthContext);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');

    try {
      // Prepare form-encoded data for FastAPI OAuth2
      const formData = new URLSearchParams();
      formData.append('username', email);  // FastAPI expects 'username'
      formData.append('password', password);
      formData.append('grant_type', 'password'); // optional for OAuth2

      const response = await axios.post(
        'http://localhost:8000/v1/auth/login',
        formData,
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        }
      );

      // Save access token in context and localStorage
      loginUser(response.data.access_token);

      // Redirect to home page
      navigate('/');
    } catch (err) {
      if (err.response && err.response.status === 401) {
        setError('Invalid credentials');
      } else if (err.response && err.response.status === 422) {
        setError('Please enter valid email and password');
      } else {
        setError('Something went wrong');
      }
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '50px auto' }}>
      <h2>Login</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleLogin}>
        <div style={{ marginBottom: '10px' }}>
          <label>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <button type="submit" style={{ padding: '10px 20px' }}>
          Login
        </button>
      </form>
    </div>
  );
}

export default LoginPage;
