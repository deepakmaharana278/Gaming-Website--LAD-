import { signInWithPopup } from "firebase/auth";
import { auth, googleProvider } from "../firebase";

export const googleLogin = async (navigate, setError) => {
  try {
    await signInWithPopup(auth, googleProvider);
    navigate("/");
  } catch (err) {
    setError(err.message);
  }
};
