import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import BusinessDetail from "./components/OneBussiness"
import AddBusiness from "./components/CreateBussinessForm";
import UpdateBusiness from "./components/UpdateBusinessForm";
import BusinessMainPage from "./components/Bussiness";
import { ModalProvider } from './context/Modal';
import OwnedBusinesses from "./components/OwnedBusiness";
function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <ModalProvider>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path="/business/all" >
            <BusinessMainPage/>
          </Route>
          <Route path="/business/:id/edit">
             <UpdateBusiness />
          </Route>
          <Route path="/business/create-new-business">
             <AddBusiness />
          </Route>
          <Route path="/business/:id">
            <BusinessDetail />
          </Route>
          <Route path="/owned">
            <OwnedBusinesses />
          </Route>


        </Switch>
      )}
    </ModalProvider>
  );
}

export default App;
