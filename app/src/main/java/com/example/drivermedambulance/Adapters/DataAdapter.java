package com.example.drivermedambulance.Adapters;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Filter;
import android.widget.Filterable;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import com.example.drivermedambulance.Model.Location;
import com.example.drivermedambulance.R;

import java.util.ArrayList;

public class DataAdapter extends RecyclerView.Adapter<DataAdapter.ViewHolder> implements Filterable {
    private ArrayList<Location> mArrayList;
    private ArrayList<Location> mFilteredList;
    Context context;
    Intent intent;

    public DataAdapter(Context context,ArrayList<Location> arrayList,Intent i) {
        mArrayList = arrayList;
        mFilteredList = arrayList;
        this.context=context;
        this.intent=i;
    }

    @Override
    public DataAdapter.ViewHolder onCreateViewHolder(ViewGroup viewGroup, int i) {
        View view = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.card_row, viewGroup, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(DataAdapter.ViewHolder viewHolder, final int i) {

        viewHolder.tv_name.setText(mFilteredList.get(i).getName());
        viewHolder.tv_version.setText(mFilteredList.get(i).getLat());
        viewHolder.tv_api_level.setText(mFilteredList.get(i).getLng());
        viewHolder.tv_add.setText(mFilteredList.get(i).getAddress());

         viewHolder.itemView.setOnClickListener(new View.OnClickListener() {
             @Override
             public void onClick(View v) {
                      if(intent!=null){
                          intent.putExtra("result",new String[]{mFilteredList.get(i).getName(),mFilteredList.get(i).getLat(),mFilteredList.get(i).getLng()});
                          ( (AppCompatActivity) context).setResult(Activity.RESULT_OK,intent);
                          ( (AppCompatActivity) context).finish();

                      }else {

                          ((AppCompatActivity) context).setResult(Activity.RESULT_CANCELED);
                          ( (AppCompatActivity) context).finish();

                      }

             }
         });


    }

    @Override
    public int getItemCount() {
        return mFilteredList.size();
    }

    @Override
    public Filter getFilter() {

        return new Filter() {
            @Override
            protected FilterResults performFiltering(CharSequence charSequence) {

                String charString = charSequence.toString();

                if (charString.isEmpty()) {

                    mFilteredList = mArrayList;
                } else {

                    ArrayList<Location> filteredList = new ArrayList<>();

                    for (Location androidVersion : mArrayList) {

                        if (androidVersion.getName().toLowerCase().contains(charString.toLowerCase()) || androidVersion.getLat().toLowerCase().contains(charString) || androidVersion.getLng().toLowerCase().contains(charString)) {

                            filteredList.add(androidVersion);
                        }
                    }

                    mFilteredList = filteredList;
                }

                FilterResults filterResults = new FilterResults();
                filterResults.values = mFilteredList;
                return filterResults;
            }

            @Override
            protected void publishResults(CharSequence charSequence, FilterResults filterResults) {
                mFilteredList = (ArrayList<Location>) filterResults.values;
                notifyDataSetChanged();
            }
        };
    }

    public class ViewHolder extends RecyclerView.ViewHolder{
        private TextView tv_name,tv_version,tv_api_level,tv_add;
        public ViewHolder(View view) {
            super(view);

            tv_name = (TextView)view.findViewById(R.id.tv_name);
            tv_version = (TextView)view.findViewById(R.id.tv_version);
            tv_api_level = (TextView)view.findViewById(R.id.tv_api_level);
            tv_add = (TextView)view.findViewById(R.id.tv_add);

        }
    }

}