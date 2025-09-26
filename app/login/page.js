"use client";
import { signIn, signOut, useSession } from "next-auth/react";
import style from './page.module.css'
import Image from "next/image";

export default function Login() {
  const { data: session } = useSession();

  if (session) {
    return (
      <>
        <p>Signed in as {session.user.email}</p>
        <button onClick={() => signOut()}>Sign out</button>
      </>
    );
  }
  return <button className={style.googlebtn} onClick={() => signIn("google")}> <Image src="/googlelogo.svg" height={30} width={40} style={{ marginLeft: "-9px" }} alt="Google Logo" ></Image> Sign in with Google</button>;
}
