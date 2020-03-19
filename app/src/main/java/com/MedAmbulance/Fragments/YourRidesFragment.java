package com.MedAmbulance.Fragments;

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

import com.MedAmbulance.Adapters.YourRideAdpter;
import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Model.YourRidesModel;
import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
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
        mrecyclerView.setHasFixedSize(true);
        mrecyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        YarrayList= new ArrayList<>();
        yourRideListAdapter=new YourRideAdpter(getContext(),YarrayList);
        mrecyclerView.setAdapter(yourRideListAdapter);
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

        Log.d("AG", "onResult: "+object);
        if (progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status){
            relativeLayout.setVisibility(View.GONE);
            Gson gson= new GsonBuilder().create();
            try {
                ArrayList<YourRidesModel> rm = gson.fromJson(object.getString("result"), new TypeToken<ArrayList<YourRidesModel>>(){}.getType());
                YarrayList.clear();
                YarrayList.addAll(rm);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            yourRideListAdapter.notifyDataSetChanged();
        }

    }
}
