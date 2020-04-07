package com.example.respondermedambulance.Comman;

import android.content.Context;
import android.util.Log;
import android.view.View;

import com.example.respondermedambulance.Api_Calling.MyResult;
import com.example.respondermedambulance.Api_Calling.OnSaveProfileResult;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.error.AuthFailureError;
import com.android.volley.error.VolleyError;
import com.android.volley.request.JsonObjectRequest;
import com.android.volley.request.SimpleMultiPartRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.lang.reflect.Field;
import java.util.ArrayList;

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
                     requestQueue.getCache().clear();

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
                    Log.d("Verifi", "onResponse: "+response);
                    try {
                        if(Boolean.parseBoolean(response.getString("status")))
                        {
                            onResult.onResult(response,true);
                        }else {

                            onResult.onResult(null,false);
                            Utility.topSnakBar(context,view, response.getString("message"));
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
    public static void postMethodCall2(final Context context, String URL, final View view, final OnSaveProfileResult onSaveProfileResult, final String name, JSONObject jsonObject) {

        if (!Utility.isNetworkConnected(context)){
            Utility.topSnakBar(context,view,Constant.NO_INTERNET);
            onSaveProfileResult.saveButtonResult(null,false);
        }else {
            JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.POST, URL, jsonObject, new Response.Listener<JSONObject>() {
                @Override
                public void onResponse(JSONObject response) {

                    Utility.log(name,response.toString());
                    Log.d("Verifi", "onResponse: "+response);
                    try {
                        if(Boolean.parseBoolean(response.getString("status")))
                        {
                            onSaveProfileResult.saveButtonResult(response,true);
                        }else {
                            onSaveProfileResult.saveButtonResult(null,false);
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

    public static void multiPartCall(final Context context, final View view, String URL, final JSONObject jsonObject, final OnSaveProfileResult onResult, final String name,ArrayList<String>path) {
        if (!Utility.isNetworkConnected(context)) {
            Utility.topSnakBar(context, view, Constant.NO_INTERNET);
        } else {
            SimpleMultiPartRequest simpleMultiPartRequest = new SimpleMultiPartRequest(Request.Method.POST, URL, new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    Utility.log(name,""+response);
                    try {
                        JSONObject jsonObject1=new JSONObject(response);
                        if(Boolean.parseBoolean(jsonObject1.getString("status"))){
                            onResult.saveButtonResult(jsonObject1,true);}else {
                            onResult.saveButtonResult(null,false);
                            Utility.topSnakBar(context,view, jsonObject1.getString("message"));
                        }
                    } catch (JSONException e) {
                        e.printStackTrace();
                        Utility.topSnakBar(context,view, Constant.SOMETHING_WENT_WRONG);
                    }
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                }
            });
            simpleMultiPartRequest.addStringParam("data",""+jsonObject.toString());
            if(path!=null && path.size()>0)
            {
                Utility.log("FinalData",""+path.get(0));
            simpleMultiPartRequest.addFile("postImage",""+new File(path.get(0)));
            }
            try {
                Utility.log("FinalData",""+simpleMultiPartRequest.getBody());
            } catch (AuthFailureError authFailureError) {
                authFailureError.printStackTrace();
            }
            RequestQueue requestQueue=Volley.newRequestQueue(context);
            requestQueue.add(simpleMultiPartRequest);
        }
    }
    public static void multiPartCall1(final Context context, final View view, String URL, final JSONObject jsonObject, final MyResult onResult, final String name,ArrayList<String>arrayList) {
        if (!Utility.isNetworkConnected(context)) {
            Utility.topSnakBar(context, view, Constant.NO_INTERNET);
        } else {
            Utility.log("Inside","Inside1");
            SimpleMultiPartRequest simpleMultiPartRequest = new SimpleMultiPartRequest(Request.Method.POST, URL, new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    Utility.log(name,""+response);
                    try {
                        Utility.log("Inside","Inside2");
                        JSONObject jsonObject1=new JSONObject(response);
                        if(Boolean.parseBoolean(jsonObject1.getString("status"))){
                            onResult.onResult(jsonObject1,true);}else {
                            onResult.onResult(null,false);
                            Utility.topSnakBar(context,view, jsonObject1.getString("message"));
                            Utility.log("Inside","Inside2");


                        }
                    } catch (JSONException e) {
                        e.printStackTrace();
                        Utility.topSnakBar(context,view, Constant.SOMETHING_WENT_WRONG);
                    }
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    Utility.log("Inside5","Inside3"+error.getMessage());
                }
            });
            simpleMultiPartRequest.addStringParam("data",""+jsonObject.toString());
            if(arrayList.size()>0)
                simpleMultiPartRequest.addFile("postImage",""+new File(arrayList.get(0).trim()));
            Utility.log("Inside3","Inside1");
            RequestQueue requestQueue=Volley.newRequestQueue(context);
            requestQueue.add(simpleMultiPartRequest);
        }
    }

}
