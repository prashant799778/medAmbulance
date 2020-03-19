package com.MedAmbulance.Adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;

import java.util.ArrayList;

public class MyTripAdapter extends RecyclerView.Adapter <MyTripAdapter.ViewHolder>{

    private Context mcontext;
    private ArrayList<myTripModel> marrayList;

    public MyTripAdapter(Context context, ArrayList<myTripModel> myTripModels) {
       mcontext=context;
       marrayList = myTripModels;
    }
    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(mcontext).inflate(R.layout.my_trip_view,parent,false);
        return new ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
     myTripModel currentItem= marrayList.get(position);
     String userName=currentItem.getUserName();
     String date =currentItem.getStartTime();
     String routeID =currentItem.getBookingId();
     holder.userName.setText(userName);
     holder.date.setText(date);
     holder.routeId.setText(routeID);
    }

    @Override
    public int getItemCount() {
        return marrayList.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{

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
