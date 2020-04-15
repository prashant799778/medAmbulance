package com.MedAmbulance.Model;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Model.SupportModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;

import java.util.ArrayList;

public class SupportAdapters extends RecyclerView.Adapter<SupportAdapters.ViewHolder> {

    private Context mcontext;
    private ArrayList<SupportModel> marrayList;

    public SupportAdapters(Context context, ArrayList<SupportModel> supportModels) {
        mcontext = context;
        marrayList = supportModels;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(mcontext).inflate(R.layout.support_item_view, parent, false);
        return new ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {

        SupportModel currentItem = marrayList.get(position);
       // String userName = currentItem.getUserName();
//        String date = currentItem.getStartTime();
//        String routeID = currentItem.getBookingId();
//        String startAddress = currentItem.getTripFrom();
//        String HospitalAddress = currentItem.getTripTo();


      //  holder.userName.setText(userName);
        if(currentItem.getStartTime()!=null)
        holder.date.setText(currentItem.getStartTime());
        if(currentItem.getId()!=null)
        holder.booking_id.setText(currentItem.getId());
        if(currentItem.getTripFrom()!=null)
        holder.startAddress.setText(currentItem.getTripFrom());
        if(currentItem.getTripTo()!=null)
            holder.hospital_address.setText(currentItem.getTripTo());

    }

    @Override
    public int getItemCount() {
        return marrayList.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {

     //   ImageView UserImage;
       // Atami_Bold userName;
        Atami_Regular fair, date, booking_id, startAddress, hospital_address;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
       //     UserImage = itemView.findViewById(R.id.user_pic);
        //    userName = itemView.findViewById(R.id.user_name);
            fair = itemView.findViewById(R.id.fair);
            booking_id = itemView.findViewById(R.id.booking_id);
            date = itemView.findViewById(R.id.date_support);
            startAddress = itemView.findViewById(R.id.start_address);
            hospital_address = itemView.findViewById(R.id.hospital_address);
        }
    }

}
