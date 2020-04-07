package com.example.drivermedambulance.Adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import com.example.drivermedambulance.R;

import java.util.List;

public class Horizontal_adapter  extends RecyclerView.Adapter<CustomRecyclerViewHolder> {

    private List<String> viewItemList;

    public Horizontal_adapter(Context context , List<String> viewItemList) {
        this.viewItemList = viewItemList;
    }

    @Override
    public CustomRecyclerViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        // Get LayoutInflater object.
        LayoutInflater layoutInflater = LayoutInflater.from(parent.getContext());
        // Inflate the RecyclerView item layout xml.
        View itemView = layoutInflater.inflate(R.layout.cab_type_item, parent, false);

        // Create and return our customRecycler View Holder object.
        CustomRecyclerViewHolder ret = new CustomRecyclerViewHolder(itemView);
        return ret;
    }

    @Override
    public void onBindViewHolder(CustomRecyclerViewHolder holder, int position) {
        if(viewItemList!=null) {
            // Get car item dto in list.
            String viewItem = viewItemList.get(position);

            if(viewItem != null) {
                // Set car item title.
               // holder.getTextView().setText(viewItem.getText());;
            }
        }
    }

    @Override
    public int getItemCount() {
        int ret = 0;
        if(viewItemList!=null)
        {
            ret = viewItemList.size();
        }
        return ret;
    }
}



   class CustomRecyclerViewHolder extends RecyclerView.ViewHolder {

    private TextView textView = null;

    public CustomRecyclerViewHolder(View itemView) {
        super(itemView);



    }

    public TextView getTextView() {
        return textView;
    }
}