if __name__ == '__main__':
    print("Starting the trainer...")
    trainer = Trainer(**configs)
    print("Trainer started. Beginning the experiment...")
    with experiment.start():
        print("Running training loop...")
        trainer.run_training_loop()
        print("Training loop finished.")
