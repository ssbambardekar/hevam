# ETL Processor Base Class
class ETLProcessorBase:
    # Constructor
    def __init__(self) -> None:
        pass

    # Normalize data frames    
    def _normalize_data_frames(self, data_frames, data_frame_columns, data_frame_column_headers):        
        try:
            # Reorder the columns as specified
            normalized_data_frames = data_frames[data_frame_columns]
            
            # Drop nulls
            normalized_data_frames.dropna(inplace = True)

            # De-dup
            normalized_data_frames.drop_duplicates(inplace = True) 

            # Normalize the columns header names
            for index, data_frame_column_header in enumerate(data_frame_column_headers):
                normalized_data_frames.rename(columns = {data_frame_columns[index] : data_frame_column_header}, inplace = True)

            return normalized_data_frames
        except Exception as error:
            print("ETL Normalizing Error: ", error)
            return data_frames
        
    # Print etl begin message
    def _print_etl_begin(self, source_file_absolute_path, processed_file_absolute_path, columns_to_be_extracted, normalized_columns_header_names):
        print("Starting ETL Processing...")
        print("Source File: ", source_file_absolute_path)
        print("Processed File: ", processed_file_absolute_path)
        print("Columns For Extraction: ", columns_to_be_extracted)
        print("Columns Headers For Normalization: ", normalized_columns_header_names)
            
    # Print etl end message
    def _print_etl_end(self):
        print("ETL Processing Completed")            

    # Print etl error message
    def _print_etl_error(self, error):
        print("ETL Processing Error: ", error)
    