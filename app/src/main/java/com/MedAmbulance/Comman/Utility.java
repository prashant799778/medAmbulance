package com.MedAmbulance.Comman;

import android.annotation.SuppressLint;
import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.util.Log;
import android.view.View;

import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;
import com.sun.easysnackbar.EasySnackBar;

public class Utility {

    public static Boolean isNetworkConnected(Context context)
    {
        ConnectivityManager manager=(ConnectivityManager)context.getApplicationContext().getSystemService(context.CONNECTIVITY_SERVICE);
        if(manager!=null){
            NetworkInfo[]info=manager.getAllNetworkInfo();
            if (info != null)
                for (int i = 0; i < info.length; i++)
                    if (info[i].getState() == NetworkInfo.State.CONNECTED) {
                        return true;
                    }
        }
        return false;
    }

    @SuppressLint("WrongConstant")
    public static void topSnakBar(Context context, View mView, String msg)
    {
        // Must create custom view in this way,so it can display normally
        if(mView!=null){
            View contentView = EasySnackBar.convertToContentView(mView, R.layout.top_snakbar);
            Atami_Regular atami_regular=contentView.findViewById(R.id.message);
            if(msg!=null)
                atami_regular.setText(msg);
            // true represent show at top,false at bottom
            EasySnackBar.make(mView, contentView, EasySnackBar.LENGTH_LONG, true).show();}
    }

    public static void log(String TAG,String TEXT)
    {
        if(TEXT!=null);
        Log.d(TAG,TEXT);
    }





}
