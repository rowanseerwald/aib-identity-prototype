from core.state_ledger import StateLedger


def main():
    ledger = StateLedger()

    # Simulated identity creation
    ledger.append(
        event_type="identity_created",
        payload={
            "aib_id": "AIB-0001",
            "creator": "rowanseerwald",
            "version": "0.1"
        }
    )

    # Simulated state change
    ledger.append(
        event_type="state_update",
        payload={
            "description": "Initial personality parameters established",
            "parameters": {
                "curiosity": 0.8,
                "stability": 0.6
            }
        }
    )

    print("Ledger integrity:", ledger.verify_integrity())
    print("Ledger state:\n")
    print(ledger.export())


if __name__ == "__main__":
    main()
