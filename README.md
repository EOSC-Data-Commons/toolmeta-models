# toolmeta-models
Database models for the tools registry

## Entity relationship diagram

```mermaid
erDiagram
    %% Root table
    TOOL_IMPLEMENTATION {
        UUID artefact_id PK
        UUID contract_id PK
        UUID concept_id FK
    }
    
    %% Artefact table
   TOOL_ARTEFACT {
        UUID id PK
        String archetype
        Text location
        JSON metadata
    }
    
    %% Tool contract table
    TOOL_CONTRACT {
        UUID id PK
        UUID concept_id FK
        String version
        Text description
        Vector embedding
    }
    
    %% Tool concept table
    TOOL_CONCEPT {
        UUID id PK
        String name
        Text description
    }
    
    %% Inputs and outputs
    TOOL_INPUT {
        UUID id PK
        UUID contract_id FK
        String name
        String modality_kind
        String modality_structure
        String[] encoding_formats
        String[] constraints
        String[] assumptions
    }
    
    TOOL_VARIABLE {
        UUID id PK
        UUID input_id FK
        String name
        String datatype
        String[] shape
    }
    
    TOOL_OUTPUT {
        UUID id PK
        UUID contract_id FK
        String name
        String modality_kind
        String encoding_format
        String[] guarantees
    }
    
    %% Relationships
    TOOL_IMPLEMENTATION ||--|| ARTEFACT : links_to
    TOOL_IMPLEMENTATION ||--|| TOOL_CONTRACT : implements
    TOOL_IMPLEMENTATION ||--|| TOOL_CONCEPT : implements
    TOOL_CONTRACT ||--|| TOOL_CONCEPT : describes
    TOOL_CONTRACT ||--o{ TOOL_INPUT : has_inputs
    TOOL_CONTRACT ||--o{ TOOL_OUTPUT : has_outputs
    TOOL_INPUT ||--o{ TOOL_VARIABLE : defines_variables
```

