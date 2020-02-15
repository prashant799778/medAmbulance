package com.MedAmbulance.Comman;

import android.content.Context;
import android.view.View;

import com.MedAmbulance.Api_Calling.MyResult;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.error.VolleyError;
import com.android.volley.request.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.JsonObject;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Api_Calling {

    public static void getMethodCall(final Context context, String URL, final View view, final MyResult onResult, final String ambulanceType, Object o)
    {
        if(!Utility.isNetworkConnected(context))
        {
            Utility.topSnakBar(context,view, Constant.NO_INTERNET);
            onResult.onResult(null,false);



        }else {

            JsonObjectRequest jsonObjectRequest=new JsonObjectRequest(Request.Method.GET, URL, null, new Response.Listener<JSONObject>() {
                @Override
                public void onResponse(JSONObject response) {
                    Utility.log(ambulanceType,response.toString());
                    try {
                        onResult.onResult(response,response.getString("status").equalsIgnoreCase("true"));
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {

                }
            });
             final RequestQueue requestQueue= Volley.newRequestQueue(context);
             requestQueue.add(jsonObjectRequest);
             requestQueue.addRequestFinishedListener(new RequestQueue.RequestFinishedListener<Object>() {
                 @Override
                 public void onRequestFinished(Request<Object> request) {

                 }
             });

        }
    }

    public static void postMethodCall(final Context context, String URL, final View view, final MyResult onResult, final String name, JSONObject jsonObject) {

        if (!Utility.isNetworkConnected(context)){
            Utility.topSnakBar(context,view,Constant.NO_INTERNET);
            onResult.onResult(null,false);
        }else {
            JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.POST, URL, jsonObject, new Response.Listener<JSONObject>() {
                @Override
                public void onResponse(JSONObject response) {


                    Utility.log(name,response.toString());
                    try {
                        if(Boolean.parseBoolean(response.getString("status")))
                        {
                            onResult.onResult(response,true);
                        }else {
                            onResult.onResult(null,false);
                        }
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {

                }
            });
            final RequestQueue requestQueue= Volley.newRequestQueue(context);
            requestQueue.add(jsonObjectRequest);
            requestQueue.addRequestFinishedListener(new RequestQueue.RequestFinishedListener<Object>() {
                @Override
                public void onRequestFinished(Request<Object> request) {

                }
            });
        }
    }

}
