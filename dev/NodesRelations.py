import styles
def elements(metadata):

    # for key, _ in  metadata.items():
    #     print(key)
    # print(metadata[key].columns)
    # number_columns=len(metadata[key].columns)
    #+" (Nb_records :"+str(jcol)+")"
    cyto_elements=[]
    for key in metadata.keys():
        if key=='tables':
            for icol, jcol in metadata[key].itertuples(index=False):
                cyto_elements.append(
                    {'data': {'id':icol, 'label': str(icol)}}
                )
        elif key=='table_columns_relations':
            for _,imere,fk,ifille,_,_ in metadata[key].itertuples(index=False):
                cyto_elements.append(
                    # {'data': {'id':imere, 'label': str(imere)}},
                    # {'data': {'id': ifille, 'label': str(ifille)}},
                    {'data': {'source': ifille, 'target': imere, 'label':str(fk)}}
                )
        # elif key=='table_columns':


    return cyto_elements