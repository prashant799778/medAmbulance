package com.MedAmbulance.Adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Model.YourRidesModel;
import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;

import java.util.ArrayList;

public class YourRideAdpter  extends RecyclerView.Adapter <YourRideAdpter.ViewHolder>{
    private Context Ycontext;
    private ArrayList<YourRidesModel> YarrayList;

//    public YourRideAdpter(Context context, ArrayList<YourRidesModel> yourRidesModels) {
//        Ycontext=context;
//        YarrayList = yourRidesModels;
//    }

    public YourRideAdpter(Context context, ArrayList<YourRidesModel> yourRidesModels) {
        Ycontext=context;
        YarrayList = yourRidesModels;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(Ycontext).inflate(R.layout.responder_trip_item_view,parent,false);
        return new YourRideAdpter.ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {

        YourRidesModel currentItem= YarrayList.get(position);

    }

    @Override
    public int getItemCount() {
        return YarrayList.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        ImageView UserImage;
        Atami_Bold userName,fair;
        Atami_Regular routeId,date;
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            UserImage=itemView.findViewById(R.id.user_pic);
            userName=itemView.findViewById(R.id.user_name);
            fair=itemView.findViewById(R.id.fair_trip);
            routeId=itemView.findViewById(R.id.route_id);
            date=itemView.findViewById(R.id.date);
        }
    }
}
