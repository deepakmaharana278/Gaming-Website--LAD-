import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getAnalytics, isSupported } from "firebase/analytics";
import { GoogleAuthProvider } from "firebase/auth";


const firebaseConfig = {
  apiKey: "AIzaSyA0avFajL-rHieQ2TSd_0QWuWhWF7d50Qg",
  authDomain: "gaming-lad-20821.firebaseapp.com",
  projectId: "gaming-lad-20821",
  storageBucket: "gaming-lad-20821.appspot.com",
  messagingSenderId: "262288238486",
  appId: "1:262288238486:web:ff93d37687cf36133e9fb7",
  measurementId: "G-RHQY2TZ67D",
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const googleProvider = new GoogleAuthProvider();

let analytics;
isSupported().then((supported) => {
  if (supported) {
    analytics = getAnalytics(app);
  }
});

export default app;
