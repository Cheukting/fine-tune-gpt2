from lighteval.logging.evaluation_tracker import EvaluationTracker
from lighteval.models.model_input import GenerationParameters
from lighteval.models.transformers.transformers_model import TransformersModelConfig
from lighteval.pipeline import ParallelismManager, Pipeline, PipelineParameters

def main():
    evaluation_tracker = EvaluationTracker(
        output_dir="./eval_results",
        save_details=True,
    )

    pipeline_params = PipelineParameters(
        launcher_type=ParallelismManager.ACCELERATE,
        custom_tasks_directory="./mathqa_task.py",
    )

    models = ["openai-community/gpt2", "./trained_model"]

    for model in models:
        model_config = TransformersModelConfig(
            model_name=model,
            batch_size=8,
            dtype="auto",
            generation_parameters=GenerationParameters(
                temperature=0.1,
                max_new_tokens=100
            )
        )

        task = "mathqa_task|3"

        pipeline = Pipeline(
            tasks=task,
            pipeline_parameters=pipeline_params,
            evaluation_tracker=evaluation_tracker,
            model_config=model_config,
        )

        pipeline.evaluate()
        pipeline.save_and_push_results()
        print(f"Model: {model}")
        print("============================")
        pipeline.show_results()
        print()

if __name__ == "__main__":
    main()