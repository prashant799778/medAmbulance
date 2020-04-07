package com.example.respondermedambulance.Comman;

import android.annotation.SuppressLint;
import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.util.Log;
import android.view.View;

import com.bumptech.glide.Glide;
import com.bumptech.glide.load.engine.DiskCacheStrategy;
import com.bumptech.glide.request.RequestOptions;
import com.example.respondermedambulance.R;
import com.example.respondermedambulance.Widget.Atami_Bold;
import com.example.respondermedambulance.Widget.Atami_Regular;
import com.sun.easysnackbar.EasySnackBar;

import org.json.JSONException;
import org.json.JSONObject;

import de.hdodenhof.circleimageview.CircleImageView;

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





    public static void setRoundedImage(Context context, CircleImageView circleImageView, String path)
    {
//        Toast.makeText(context, "Before", Toast.LENGTH_SHORT).show();
        Glide.with(context).load(path).
                apply(RequestOptions.skipMemoryCacheOf(true)).apply(RequestOptions.encodeQualityOf(100))
                .apply(RequestOptions.diskCacheStrategyOf(DiskCacheStrategy.NONE)).into(circleImageView);
//        Toast.makeText(context, "After", Toast.LENGTH_SHORT).show();
    }

    public static String getValueFromJsonObject(JSONObject jsonObject, String key) {
        String s = "";
        if (jsonObject.has(key)) {
            try {
                s = jsonObject.getString(key);
                if (s.equalsIgnoreCase(null)) {
                    s = "";
                }
            } catch (JSONException e) {
                e.printStackTrace();
            } finally {
                return s;
            }
        }
        return s;
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
