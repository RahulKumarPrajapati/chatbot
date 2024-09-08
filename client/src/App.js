import Chat from './components/header/chat/Chat';
import Header from './components/header/Header';
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css'
import 'font-awesome/css/font-awesome.min.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<Navigate to="/chat" replace />} />
          <Route path='/chat' element={<Chat/>}/>
        </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
