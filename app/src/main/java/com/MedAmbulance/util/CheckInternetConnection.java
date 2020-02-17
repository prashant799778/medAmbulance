package com.MedAmbulance.util;

import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;

public class CheckInternetConnection 
{
	Context context;
	public CheckInternetConnection(Context ctx) 
	{
		this.context=ctx;
	}
	public static boolean isNetworkAvailable(Context context)
	{
	     ConnectivityManager connectivityManager = (ConnectivityManager)context.getSystemService(Context.CONNECTIVITY_SERVICE);
	     NetworkInfo activeNetworkInfo = connectivityManager.getActiveNetworkInfo();
	     return activeNetworkInfo != null && activeNetworkInfo.isConnectedOrConnecting();
	}
}
