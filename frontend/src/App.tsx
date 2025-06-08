import './utils/chart';

import { Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard/Dashboard';
import Team from './pages/Team/Team';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Team />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="*" element={<Team />} />
    </Routes>
  );
};

export default App;
