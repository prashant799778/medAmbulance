package com.example.respondermedambulance.Fragments;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RelativeLayout;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.respondermedambulance.Adapters.YourRideAdpter;
import com.example.respondermedambulance.Adapters.YourRideAdpter1;
import com.example.respondermedambulance.Api_Calling.MyResult;
import com.example.respondermedambulance.Comman.Api_Calling;
import com.example.respondermedambulance.Comman.MySharedPrefrence;
import com.example.respondermedambulance.Comman.URLS;
import com.example.respondermedambulance.Comman.Utility;
import com.example.respondermedambulance.Model.YourRidesModel;
import com.example.respondermedambulance.Model.myTripModel;
import com.example.respondermedambulance.R;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class YourRidesFragment extends Fragment implements MyResult {

    MyResult myResult;
    MySharedPrefrence m;
    ProgressDialog progressDialog;

    private RecyclerView mrecyclerView;
    private YourRideAdpter yourRideListAdapter;
    RelativeLayout relativeLayout;
    private ArrayList<YourRidesModel> YarrayList;


    private RecyclerView mrecyclerView1;
    private YourRideAdpter1 yourRideListAdapter1;
    private ArrayList<YourRidesModel> YarrayList1;

    public YourRidesFragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        m = MySharedPrefrence.instanceOf(getContext());
        this.myResult=this;
        View rootView = inflater.inflate(R.layout.frag_your_ride, container, false);
        relativeLayout=rootView.findViewById(R.id.no_data);
        progressDialog = new ProgressDialog(getContext());
        progressDialog.setMessage(" Please wait ...");
        progressDialog.setCancelable(true);
        progressDialog.show();
        mrecyclerView=rootView.findViewById(R.id.Your_Ride);
        mrecyclerView.setLayoutManager(new LinearLayoutManager(getContext()));

        mrecyclerView1=rootView.findViewById(R.id.Your_Ride1);
        mrecyclerView1.setLayoutManager(new LinearLayoutManager(getContext()));


        YarrayList= new ArrayList<>();
        yourRideListAdapter=new YourRideAdpter(getContext(),YarrayList);
        mrecyclerView.setAdapter(yourRideListAdapter);



        YarrayList1= new ArrayList<>();
        yourRideListAdapter1=new YourRideAdpter1(getContext(),YarrayList1);
        mrecyclerView1.setAdapter(yourRideListAdapter1);



        Api_Calling.postMethodCall(getContext(), URLS.YOUR_RIDE,getActivity().getWindow().getDecorView().getRootView(),myResult,"Mytrip",YourRideObject());
        return rootView;
    }

    private JSONObject YourRideObject() {
        int startLimit=0,endLimit=10;
        JSONObject jsonObject=new JSONObject();

        try {
            jsonObject.put("userId",""+m.getUserId())
            .put("startLimit",""+startLimit)
                    .put("endLimit",""+endLimit);

            Log.d("Mytrip", "profileObject: "+jsonObject);

        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;
    }

    @Override
    public void onResult(JSONObject object, Boolean status) {

        Log.d("AGiiiiiiiiiiiiiiiiii", "onResult: "+object);
        if (progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status){
            relativeLayout.setVisibility(View.GONE);
            Gson gson= new GsonBuilder().create();
            try {
                if(object.getJSONObject("result").getJSONArray("ambulance").length()>0){
                ArrayList<YourRidesModel> rm = gson.fromJson(object.getJSONObject("result").getString("ambulance"), new TypeToken<ArrayList<YourRidesModel>>(){}.getType());
                YarrayList.clear();
                YarrayList.addAll(rm);
                    Utility.log("ArraySize","---1--"+rm.size());
                yourRideListAdapter.notifyDataSetChanged();}
                if(object.getJSONObject("result").getJSONArray("responder").length()>0){
                ArrayList<YourRidesModel> rm1 = gson.fromJson(object.getJSONObject("result").getString("responder"), new TypeToken<ArrayList<YourRidesModel>>(){}.getType());
                YarrayList1.clear();
                YarrayList1.addAll(rm1);
                    Utility.log("ArraySize","---"+rm1.size());
                yourRideListAdapter1.notifyDataSetChanged();
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }

        }

    }
}
